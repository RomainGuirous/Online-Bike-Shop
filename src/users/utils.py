from db_api import DBConnection
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
    sql = "SELECT * FROM user"
    cursor = db_connection.new_cursor()
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
    return pd.DataFrame(users)
