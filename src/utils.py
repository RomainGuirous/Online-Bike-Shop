# utility functions for the application
# database import

from database import create_connection, close_connection
from config import DB_FILE


def add_bike_data(bike_data: dict) -> None:
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO bikes (name, description, price) VALUES (?, ?, ?)",
            (bike_data["name"], bike_data["description"], bike_data["price"]),
        )
        conn.commit()
        close_connection(conn)
    else:
        print("Failed to connect to the database.")
        print("Failed to add bike data.")
