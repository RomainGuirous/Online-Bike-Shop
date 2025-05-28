from db_api import DBConnection
from products.models import Product
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()


def get_product_list_model(db_connection: DBConnection, product_id: int = None) -> list:
    """
    Retrieve a list of Product models from the database.
    This function fetches product data from the database and converts it into a list of Product models.
    If a product_id is provided, it retrieves only that specific product.
    If no product_id is provided, it retrieves all products.

    Args:
        db_connection (DBConnection): The database connection object.
        product_id (int, optional): The ID of the product to retrieve. Defaults to None.

    Returns:
        list: A list of Product models.
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
    if os.getenv("CONNECTION_TYPE") == "nosql":
        products_list = db_connection.find("product")
        products = []
        for product in products_list:
            product_data = {
                "product_id": product.get("product_id"),
                "product_name": product.get("product_name"),
                "product_description": product.get("product_description"),
                "price": product.get("price"),
                "picture": product.get("picture"),
                "spetech": product.get("spetech"),
            }
            products.append(product_data)
        return products
    elif os.getenv("CONNECTION_TYPE") == "sql":
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
    Retrieve a list of the best-selling products from the database.
    This function fetches the top 4 products based on the total quantity sold.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        list: A list of dictionaries containing product details.
    """
    if os.getenv("CONNECTION_TYPE") == "nosql":
        # If using NoSQL, fetch best-selling products from the collection
        products_list = db_connection.find("orderdetail")
        product_sales = {}
        for order in products_list:
            product_id = order.get("product_id")
            quantity = order.get("quantity", 0)
            if product_id in product_sales:
                product_sales[product_id] += quantity
            else:
                product_sales[product_id] = quantity

        # Sort products by total quantity sold and get the top 4
        sorted_products = sorted(
            product_sales.items(), key=lambda x: x[1], reverse=True
        )[:4]
        product_ids = [product[0] for product in sorted_products]

        # Fetch product details for the top products
        products = db_connection.find("product", {"product_id": {"$in": product_ids}})
        return [product for product in products if product["product_id"] in product_ids]

    if os.getenv("CONNECTION_TYPE") == "sql":
        # SQL implementation to get best-selling products
        # Get the top 4 products based on total quantity sold
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

        # Fetch product details for the top products
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
    Retrieve a list of spetechs from the database.
    This function fetches spetech data from the database and returns it as a list of dictionaries.
    If a spetech_id is provided, it retrieves only that specific spetech.
    If no spetech_id is provided, it retrieves all spetechs.

    Args:
        db_connection (DBConnection): The database connection object.
        spetech_id (int, optional): The ID of the spetech to retrieve. Defaults to None.

    Returns:
        list: A list of spetechs.
    """
    if os.getenv("CONNECTION_TYPE") == "nosql":
        # If using NoSQL, fetch spetechs from the collection
        spetechs_list = db_connection.find("spetech")
        spetechs = []
        for spetech in spetechs_list:
            spetech_data = {
                "spetech_id": spetech.get("spetech_id"),
                "spetech_type": spetech.get("spetech_type"),
                "color": spetech.get("color"),
                "spetech_weight": spetech.get("spetech_weight"),
                "brand": spetech.get("brand"),
                "frame_size": spetech.get("frame_size"),
            }
            if not spetech_id or spetech_data["spetech_id"] == spetech_id:
                spetechs.append(spetech_data)
    elif os.getenv("CONNECTION_TYPE") == "sql":
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
    This function fetches product data from the database and returns it as a pandas DataFrame.
    If a product_id is provided, it retrieves only that specific product.
    If no product_id is provided, it retrieves all products.

    Args:
        db_connection (DBConnection): The database connection object.
        product_id (int, optional): The ID of the product to retrieve. Defaults to None.

    Returns:
        pd.DataFrame: A DataFrame containing product data.
    """
    if os.getenv("CONNECTION_TYPE") == "nosql":
        # If using NoSQL, fetch products from the collection
        products_list = db_connection.find("product")
        products = []
        for product in products_list:
            if product_id and product.get("product_id") != product_id:
                continue
            product_data = {
                "product_id": product.get("product_id"),
                "product_name": product.get("product_name"),
                "product_description": product.get("product_description"),
                "price": product.get("price"),
                "picture": product.get("picture"),
                "spetech": product.get("spetech"),
            }
            products.append(product_data)
    elif os.getenv("CONNECTION_TYPE") == "sql":
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
