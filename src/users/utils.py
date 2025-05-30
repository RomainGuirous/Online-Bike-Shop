from db_api import DBConnection, ConnectionType
import pandas as pd

def get_user_list(db_connection: DBConnection) -> pd.DataFrame:
    """
    Retrieve a DataFrame of all users from the database.
    This function fetches user data from the database and converts it into a DataFrame.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all users.
    """
    if db_connection.connection_type == ConnectionType.SQLITE:
        sql = "SELECT * FROM user"
        cursor = db_connection.new_query()
        dataset = cursor.execute(sql)
        users = []
        for row in dataset:
            user = {
                "user_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
            }
            users.append(user)
    elif db_connection.connection_type == ConnectionType.MONGODB:
        users_list = db_connection.new_query()['User'].find()
        users = []
        for user in users_list:
            user_data = {
                "user_id": user.get("user_id"),
                "first_name": user.get("first_name"),
                "last_name": user.get("last_name"),
                "email": user.get("email"),
            }
            users.append(user_data)
    return pd.DataFrame(users)


def register_user(db_connection: DBConnection, user_data: dict) -> None:
    """
    Register a new user in the database.
    This function inserts a new user record into the database.

    Args:
        db_connection (DBConnection): The database connection object.
        user_data (dict): A dictionary containing user data with keys 'first_name', 'last_name', 'email'.

    Returns:
        None
    """
    if db_connection.connection_type == ConnectionType.SQLITE:
        sql = "INSERT INTO user (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"
        db_connection.new_cursor().execute(sql, user_data)
    elif db_connection.connection_type == ConnectionType.MONGODB:
        db_connection.insert("user", user_data)


def get_user_by_id(db_connection: DBConnection, user_id: int) -> dict:
    """
    Retrieve a user from the database by their ID.
    This function fetches user data from the database and returns it as a dictionary.

    Args:
        db_connection (DBConnection): The database connection object.
        user_id (int): The ID of the user to retrieve.

    Returns:
        dict: A dictionary containing user data or an empty dictionary if not found.
    """
    if db_connection.connection_type == ConnectionType.SQLITE:
        sql = "SELECT * FROM user WHERE user_id = :user_id"
        cursor = db_connection.new_cursor()
        cursor.execute(sql, {"user_id": user_id})
        row = cursor.fetchone()
        if row:
            return {
                "user_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "email": row[3],
            }
    elif db_connection.connection_type == ConnectionType.MONGODB:
        user = db_connection.find_one("user", {"user_id": user_id})
        if user:
            return {
                "user_id": user.get("user_id"),
                "first_name": user.get("first_name"),
                "last_name": user.get("last_name"),
                "email": user.get("email"),
            }
    return {}


def update_user(db_connection: DBConnection, user_id: int, user_data: dict) -> None:
    """
    Update an existing user in the database.
    This function updates user data in the database based on the provided user ID.

    Args:
        db_connection (DBConnection): The database connection object.
        user_id (int): The ID of the user to update.
        user_data (dict): A dictionary containing updated user data with keys 'first_name', 'last_name', 'email'.

    Returns:
        None
    """
    if db_connection.connection_type == ConnectionType.SQLITE:
        sql = "UPDATE user SET first_name = :first_name, last_name = :last_name, email = :email WHERE user_id = :user_id"
        user_data["user_id"] = user_id
        db_connection.new_cursor().execute(sql, user_data)
    elif db_connection.connection_type == ConnectionType.MONGODB:
        db_connection.update("user", {"user_id": user_id}, user_data)
