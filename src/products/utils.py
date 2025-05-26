from db_api import DBConnection

# product list to Pydantic model
from products.models import Product
import pandas as pd


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


def get_product_list(
    db_connection: DBConnection, product_id: int = None
) -> list[dict[str]]:
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
            "product_name": row[1],
            "product_description": row[2],
            "price": row[3],
            "picture": row[4],
            "spetech": row[5],
        }
        products.append(product)
    return products


def get_best_selling_products(db_connection: DBConnection) -> list[dict[str]]:
    """
    Retrieve a list of best-selling products from the database.
    Args:
        db_connection (DBConnection): The database connection object.
    Returns:
        list: A list of best-selling products.
    """

    # get the best-selling products
    sql = """
    SELECT product_id, SUM(quantity) as total_quantity
    FROM orderdetail
    GROUP BY product_id
    ORDER BY total_quantity DESC
    LIMIT 4
    """
    cursor = db_connection.new_cursor()
    dataset = cursor.execute(sql)
    products = []
    for row in dataset:
        product = {
            "product_id": row[0],
            "quantity": row[1],
        }
        products.append(product)

    # get thr products with product_id
    sql = """
    SELECT product_id, product_name, product_description, price, picture
    FROM product
    WHERE product_id IN ({})
    """.format(",".join([str(product["product_id"]) for product in products]))
    cursor = db_connection.new_cursor()
    dataset = cursor.execute(sql)
    products = []
    for row in dataset:
        product = {
            "product_id": row[0],
            "product_name": row[1],
            "product_description": row[2],
            "price": row[3],
            "picture": row[4],
        }
        products.append(product)
    return products


def get_spetech_list(
    db_connection: DBConnection, spetech_id: int = None
) -> list[dict[str]]:
    """
    Retrieve a list of products from the database.
    Args:
        db_connection (DBConnection): The database connection object.
        product_id (int, optional): The ID of the product to retrieve. Defaults to None.
    Returns:
        list: A list of products.
    """
    sql = "SELECT * FROM SpeTech"
    if spetech_id:
        sql += f" WHERE spetech_id = {spetech_id}"
    cursor = db_connection.new_cursor()
    dataset = cursor.execute(sql)
    spetechs = []
    for row in dataset:
        spetech = {
            "spetech_id": row[0],
            "spetech_type": row[1],
            "color": row[2],
            "spetech_weight": row[3],
            "brand": row[4],
            "frame_size": row[5],
        }
        spetechs.append(spetech)
    return spetechs


def get_product_dataframe(
    db_connection: DBConnection, product_id: int = None
) -> pd.DataFrame:
    """
    Retrieve a DataFrame of products from the database.
    Args:
        db_connection (DBConnection): The database connection object.
        product_id (int, optional): The ID of the product to retrieve. Defaults to None.
    Returns:
        pd.DataFrame: A DataFrame containing the products.
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
            "product_name": row[1],
            "product_description": row[2],
            "price": row[3],
            "picture": row[4],
            "spetech": row[5],
        }
        products.append(product)
    return pd.DataFrame(products)
