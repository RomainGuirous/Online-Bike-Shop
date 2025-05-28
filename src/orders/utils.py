# get all orders
from db_api import DBConnection
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()


def get_orderhead_list(db_connection: DBConnection) -> pd.DataFrame:
    """
    Retrieve a DataFrame of all orders from the database.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all orders.
    """
    if os.getenv("CONNECTION_TYPE") == "nosql":
        # If using NoSQL, fetch orders from the collection
        orders_list = db_connection.find("orderhead")
        orders = []
        for order in orders_list:
            order_data = {
                "orderhead_id": order.get("orderhead_id"),
                "orderhead_date": order.get("orderhead_date"),
                "user_id": order.get("user_id"),
            }
            orders.append(order_data)
        return pd.DataFrame(orders)
    elif os.getenv("CONNECTION_TYPE") == "sql":
        sql = "SELECT * FROM orderhead"
        cursor = db_connection.new_query()
        dataset = cursor.execute(sql)
        orders = []
        for row in dataset:
            order = {
                "orderhead_id": row[0],
                "orderhead_date": row[1],
                "user_id": row[2],
            }
            orders.append(order)
    return pd.DataFrame(orders)


def get_orderdetails_list(db_connection: DBConnection) -> pd.DataFrame:
    """
    Retrieve a DataFrame of all orders from the database.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all orders.
    """
    if os.getenv("CONNECTION_TYPE") == "nosql":
        # If using NoSQL, fetch order details from the collection
        orders_list = db_connection.find("orderdetail")
        orders = []
        for order in orders_list:
            order_data = {
                "orderdetail_id": order.get("orderdetail_id"),
                "product_id": order.get("product_id"),
                "quantity": order.get("quantity"),
            }
            orders.append(order_data)
    elif os.getenv("CONNECTION_TYPE") == "sql":
        sql = "SELECT * FROM orderdetail"
        cursor = db_connection.new_query()
        dataset = cursor.execute(sql)
        orders = []
        for row in dataset:
            order = {"orderdetail_id": row[0], "product_id": row[1], "quantity": row[2]}
            orders.append(order)
    return pd.DataFrame(orders)


def get_order_list(db: DBConnection) -> pd.DataFrame:
    """
    Merge order head and order detail DataFrames.

    Args:
        db (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A merged DataFrame containing all orders.
    """

    orders_head = get_orderhead_list(db)
    orders_detail = get_orderdetails_list(db)

    merged_orders = pd.merge(
        orders_head,
        orders_detail,
        left_on="orderhead_id",
        right_on="orderdetail_id",
        how="inner",
    )
    return merged_orders
