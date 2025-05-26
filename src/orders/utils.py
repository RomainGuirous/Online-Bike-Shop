# get all orders
from db_api import DBConnection
import pandas as pd


def get_orderhead_list(db_connection: DBConnection) -> pd.DataFrame:
    """
    Retrieve a DataFrame of all orders from the database.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all orders.
    """
    sql = "SELECT * FROM orderhead"
    cursor = db_connection.new_cursor()
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
    sql = "SELECT * FROM orderdetail"
    cursor = db_connection.new_cursor()
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
