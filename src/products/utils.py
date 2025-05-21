from db_api import DBConnection

# product list to Pydantic model
from products.models import Product

def get_product_list_model(db_connection: DBConnection, product_id: int = None) -> list:
    """
    Retrieve a list of products from the database and convert them to Pydantic models.

    Args:
        db_connection (DBConnection): The database connection object.
        product_id (int, optional): The ID of the product to retrieve. Defaults to None.

    Returns:
        list: A list of Pydantic product models.
    """
    products = get_product_list(db_connection, product_id)
    return [Product(**product) for product in products]

def get_product_list(db_connection: DBConnection, product_id: int = None) -> list:
    """
    Retrieve a list of products from the database.
    Args:
        db_connection (DBConnection): The database connection object.
        product_id (int, optional): The ID of the product to retrieve. Defaults to None.
    Returns:
        list: A list of products.
    """ 
    sql = "SELECT * FROM product"
    if product_id:
        sql += f" WHERE product_id = {product_id}"
    cursor = db_connection.new_cursor()
    dataset = cursor.execute(sql)
    products = []
    for row in dataset:
        product = {
            "product_id": row[0],
            "name": row[1],
            "description": row[2],
            "technical_details": row[3],
            "price": row[4],
            "picture": row[5]
        }
        products.append(product)
    return products