# get all orders
from db_api import DBConnection, ConnectionType
import pandas as pd


def get_orderhead_list(db_connection: DBConnection) -> pd.DataFrame:
    """
    Retrieve a DataFrame of all order heads from the database.
    If using NoSQL, it fetches from the MongoDB collection.
    If using SQL, it executes a query to fetch from the SQLite database.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all order heads.
    """
    if db_connection.connection_type == ConnectionType.MONGODB:
        # If using NoSQL, fetch orders from the collection
        orders_list = db_connection.new_query()["OrderHead"].find()
        orders = []
        # order_details = []
        for order in orders_list:
            order_data = {
                "orderhead_id": order.get("_id"),
                "orderhead_date": order.get("orderhead_date"),
                "user_id": order.get("user_id"),
                "OrderDetails": order.get("OrderDetails", []),
            }

            orders.append(order_data)
        # for order in orders:
        #     for detail in order["OrderDetails"]:
        #         order_detail = {
        #             "product_id": detail.get("product_id"),
        #             "quantity": detail.get("quantity"),
        #         }
        #         order_details.append(order_detail)
        #     del order["OrderDetails"]
        # return pd.DataFrame(orders), pd.DataFrame(order_details)
        orders = pd.json_normalize(
            orders,
            record_path=['OrderDetails'],
            meta=['orderhead_id', 'orderhead_date', 'user_id']
        )

        return orders
    elif db_connection.connection_type == ConnectionType.SQLITE:
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
    Retrieve a DataFrame of all order details from the database.
    If using NoSQL, it fetches from the MongoDB collection.
    If using SQL, it executes a query to fetch from the SQLite database.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all order details.
    """
    if db_connection.connection_type == ConnectionType.MONGODB:
        # If using NoSQL, fetch order details from the collection
        orders_list = db_connection.new_query()["orderdetail"].find()
        orders = []
        for order in orders_list:
            order_data = {
                "orderdetail_id": order.get("orderdetail_id"),
                "product_id": order.get("product_id"),
                "quantity": order.get("quantity"),
            }
            orders.append(order_data)
    elif db_connection.connection_type == ConnectionType.SQLITE:
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
    Retrieve a DataFrame of all orders by merging order heads and order details.
    This function fetches order heads and details from the database,
    merges them on their respective IDs, and returns the combined DataFrame.

    Args:
        db (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing merged order heads and details.
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
