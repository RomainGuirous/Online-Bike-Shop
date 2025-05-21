# Product model definitions
from products.schemas import ProductBase

class Product(ProductBase):
    """
    Product model representing a product in the database.
    """
    def __init__(self, product_id, name, description, technical_details, price):
        super().__init__(
            product_id=product_id,
            name=name,
            description=description,
            technical_details=technical_details,
            price=price
        )
        

# product = Product(
#     product_id=1,
#     name="Moun",
#     description="A high-performance mountain bike.",
#     technical_details="Frame: Aluminum, Gears: 21-speed, Brakes: Disc",
#     price=499.99
# )

# print(product)
    
    
