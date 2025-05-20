from pydantic import BaseModel, Field


class OrderBase(BaseModel):
    order_id: int = Field(..., description="Unique identifier for the order")
    user_id: int = Field(..., description="Unique identifier for the user")
    product_id: int = Field(..., description="Unique identifier for the product")
    quantity: int = Field(..., description="Quantity of the product ordered")
