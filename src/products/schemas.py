from pydantic import BaseModel, Field

class ProductBase(BaseModel):
    product_id: int = Field(..., description="Unique identifier for the product")
    name: str = Field(..., description="Name of the product")
    description: str = Field(..., description="Description of the product")
    technical_details: str = Field(..., description="Technical details of the product")
    price: float = Field(..., description="Price of the product")