from database import load_product_data, save_product_data
from product_schema import Product , UpdateProduct
from fastapi import HTTPException

# Post : Create Product
def create_product(product: Product):
    data = load_product_data()
    if product.prod_id in data:
        raise HTTPException(status_code=400, detail="Product alreaady exists")
    
    data[product.prod_id] = product.model_dump(exclude={'prod_id'})
    save_product_data(data)

# GET : All product
def view_products():
    data = load_product_data()
    if data ==  {}:
        return []
    return data

# GET: Get product by id
def product_by_id(prod_id:str):
    data = load_product_data()
    if prod_id not in data:
        raise HTTPException(status_code=404, detail="Product not found")
    return data[prod_id]

# PUT : Update product
def update_product(prod_id:str , product_update: UpdateProduct):
    data = load_product_data()
    if prod_id not in data:
        raise HTTPException(status_code=404, detail="Product not found")
    
    existing_product_info = data[prod_id]
    updated_product_info = product_update.model_dump(exclude_unset=True)

    for key, value in updated_product_info.items():
        existing_product_info[key] = value

    existing_product_info["prod_id"] = prod_id
    product_obj = Product(**existing_product_info)

    data[prod_id] = product_obj.model_dump(exclude={"prod_id"})
    save_product_data(data)

# DELETE : Delete product
def del_product(prod_id:str):
    data = load_product_data()
    if prod_id not in data:
        raise HTTPException(status_code=404, detail="Product not found")
    
    del data[prod_id]
    save_product_data(data)