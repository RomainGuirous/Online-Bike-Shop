# db connection related stuff

from sqlite3 import connect
from sqlite3 import Connection
from sqlite3 import Error


def create_connection(db_file: str) -> Connection:
    """create a database connection to a SQLite database"""
    conn = None
    try:
        conn = connect(db_file)
        print(f"Connection to {db_file} successful.")
    except Error as e:
        print(e)
    return conn


def close_connection(conn: Connection) -> None:
    """close the database connection"""
    if conn:
        conn.close()
        print("Connection closed.")
    else:
        print("No connection to close.")
