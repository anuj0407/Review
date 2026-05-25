from pydantic import BaseModel, Field
from typing import Optional, Annotated

class Product(BaseModel):

    prod_id: Annotated[int,Field(..., description="Product ID",examples=[1,101])]
    name: Annotated[str,Field(...,description="Product Name")]
    description: Annotated[Optional[str],Field(description="Product description")]
    price: Annotated[float,Field(..., description="Product price", gt=0)]
    stock: Annotated[int,Field(...,description="Product Quanity in stock", ge=0)]
    category: Annotated[str,Field(..., description="Category of the product",examples=["electronics","clothing"])]

class UpdateProduct(BaseModel):
    
    name: Annotated[Optional[str],Field(description="Product Name")]
    description: Annotated[Optional[str],Field(description="Product description")]
    price: Annotated[Optional[float],Field(description="Product price", gt=0)]
    stock: Annotated[Optional[int],Field(description="Product Quanity in stock", ge=0)]
    category: Annotated[Optional[str],Field(description="Category of the product",examples=["electronics","clothing"])]
