from db_api import DBConnection
import pandas as pd
import os
import dotenv

dotenv.load_dotenv()


def get_user_list(db_connection: DBConnection) -> pd.DataFrame:
    """
    Retrieve a DataFrame of all users from the database.
    This function fetches user data from the database and converts it into a DataFrame.

    Args:
        db_connection (DBConnection): The database connection object.

    Returns:
        pd.DataFrame: A DataFrame containing all users.
    """
    if os.getenv("CONNECTION_TYPE") == "sql":
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
    elif os.getenv("CONNECTION_TYPE") == "nosql":
        users_list = db_connection.find_all("user")
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
