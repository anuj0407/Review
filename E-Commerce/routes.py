import crud
from fastapi import APIRouter
from product_schema import Product, UpdateProduct
from fastapi.responses import JSONResponse
from database import load_product_data

router = APIRouter()

# GET: Home page
@router.get("/")
def home():
    return {"Message": "Welcome to E-Commerce API"}

# POST : create products
@router.post("/products")
def create_product(product: Product):
    crud.create_product(product)
    return JSONResponse(status_code=201, content={"Message":"Product created Successfully"})

# GET : get all products
@router.get("/view_products")
def view_products():
    return crud.view_products()

# GET : get product by id
@router.get("/view_products/{prod_id}")
def product_by_id(prod_id: str):
    return crud.product_by_id(prod_id)

# PUT : update product
@router.put("/products/{id}")
def update_product(prod_id: str, updated_product: UpdateProduct):
    crud.update_product(prod_id, updated_product) 
    data = load_product_data()
    return data[prod_id]

# DELETE : delete product
@router.delete("/remove_product/{id}")
def remove_product(prod_id: str):
    crud.del_product(prod_id)
    return JSONResponse(status_code=200, content={"Message":"Product deleted successfully"})