# get all orders
from db_api import DBConnection, create_connection
import pandas as pd


conn = create_connection()

def get_all_orders_head(db_connection: DBConnection) -> pd.DataFrame:
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
            "order_id": row[0],

        }
        orders.append(order)
    return pd.DataFrame(orders)

def get_all_orders_detail(db_connection: DBConnection) -> pd.DataFrame:
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
        order = {
            "order_id": row[0],
            "product_id": row[1],
            "quantity": row[2]
        }
        orders.append(order)
    return pd.DataFrame(orders)