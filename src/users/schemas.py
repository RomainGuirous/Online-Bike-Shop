from pydantic import BaseModel, Field, EmailStr

class UserBase(BaseModel):
    user_id: int = Field(..., description="Unique identifier for the user")
    username: str = Field(..., description="Username of the user")
    email: EmailStr
    first_name: str = Field(..., description="First name of the user")
    last_name: str = Field(..., description="Last name of the user")
