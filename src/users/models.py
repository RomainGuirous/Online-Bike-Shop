from schemas import UserBase

class User(UserBase):
    """
    User model representing a user in the database.
    """
    def __init__(self, user_id, username, email, first_name, last_name):
        super().__init__(
            user_id=user_id,
            username=username,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
user = User(
    user_id=1,
    username="john_doe",
    email="john@example.com",
    first_name="John",
    last_name="Doe"
)
