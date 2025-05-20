# Product model definitions

class Product:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def __str__(self):
        return f"Product(name={self.name}, price={self.price}, description={self.description})"
    
    