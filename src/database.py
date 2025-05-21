# db connection related stuff

from sqlite3 import connect
from sqlite3 import Connection
from sqlite3 import Error


# region connection


def create_connection(db_file: str) -> Connection:
    """
    Create a database connection to a SQLite database.

    Args:
        db_file (str): The database file path.

    Returns:
        Connection: Connection object or None if connection fails.
    """
    conn = None
    try:
        conn = connect(db_file)
        print(f"Connection to {db_file} successful.")
    except Error as e:
        print(e)
    return conn


# region deconnection


def close_connection(conn: Connection) -> None:
    """
    Close the database connection.

    Args:
        conn (Connection): The connection object to close.

    Returns:
        None
    """
    if conn:
        conn.close()
        print("Connection closed.")
    else:
        print("No connection to close.")
