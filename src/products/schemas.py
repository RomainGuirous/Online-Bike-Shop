from pydantic import BaseModel, Field


class ProductBase(BaseModel):
    product_id: int = Field(..., description="Unique identifier for the product")
    name: str = Field(min_length=1, max_length=100, description="Name of the product")
    description: str = Field(..., description="Description of the product")
    technical_details: str = Field(..., description="Technical details of the product")
    price: float = Field(..., description="Price of the product")
    picture: str = Field(..., description="Picture URL of the product")

