# utility functions for the application
# database import

from .database import create_connection, close_connection
import faker as fk
from .config import (
    DB_FILE,
    NBR_USERS,
    NBR_PRODUCTS,
    NBR_SPETECH,
    NBR_ORDERS,
    NBR_ORDERDETAIL,
)

# region add product


def add_product_data(product_data: dict) -> None:
    """
    Add  1 product data to the database.

    Args:
        product_data (dict): A dictionary containing product data.
        The dictionary should contain the following keys:
            - product_name: str
            - description: str
            - price: str
            - picture: str

    Returns:
        None
    """
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Product(product_name, description, price, picture) VALUES (?, ?, ?, ?)",
            (
                product_data["product_name"],
                product_data["description"],
                product_data["price"],
                product_data["picture"],
            ),
        )
        conn.commit()
        close_connection(conn)
    else:
        print("Failed to connect to the database.")
        print("Failed to add product data.")


# region add user


def add_user_data(user_data: dict) -> None:
    """
    Add  1 user data to the database.

    Args:
        product_data (dict): A dictionary containing product data.
        The dictionary should contain the following keys:
            - first_name: str
            - last_name: str
            - email: str

    Returns:
        None
    """
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO User(first_name, last_name, email) VALUES (?, ?, ?)",
            (
                user_data["first_name"],
                user_data["last_name"],
                user_data["email"],
            ),
        )
        conn.commit()
        close_connection(conn)
    else:
        print("Failed to connect to the database.")
        print("Failed to add user data.")


# region add order


def add_order_data(order_data: dict) -> None:
    """
    Add  1 user data to the database.

    Args:
        product_data (dict): A dictionary containing product data.
        The dictionary should contain the following keys:
            - date: str
            - quantity: str
            - user_id: str

    Returns:
        None
    """
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO User(date, quantity, user_id) VALUES (?, ?, ?)",
            (
                order_data["date"],
                order_data["quantity"],
                order_data["user_id"],
            ),
        )
        conn.commit()
        close_connection(conn)
    else:
        print("Failed to connect to the database.")
        print("Failed to add order data.")


# region add spetech


def add_spetech_data(spetech_data: dict) -> None:
    """
    Add  1 spetech data to the database.

    Args:
        product_data (dict): A dictionary containing product data.
        The dictionary should contain the following keys:
            - type: str
            - color: str
            - weight: str
            - brand: str
            - frame_size: str

    Returns:
        None
    """
    conn = create_connection(DB_FILE)
    if conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Spetech(type, color, weight, brand, frame_size) VALUES (?, ?, ?, ?, ?)",
            (
                spetech_data["type"],
                spetech_data["color"],
                spetech_data["weight"],
                spetech_data["brand"],
                spetech_data["frame_size"],
            ),
        )
        conn.commit()
        close_connection(conn)
    else:
        print("Failed to connect to the database.")
        print("Failed to add spetech data.")


# region faker user


def generate_fake_user(nbr_users: int = NBR_USERS) -> list[dict[str, str]]:
    """
    Generate fake user data using the Faker library.

    Args:
        nbr_users (int): The number of fake users to generate.

    Returns:
        list: A list of dictionaries containing fake user data.
    """
    fake = fk.Faker()
    fake_users = []
    for _ in range(nbr_users):
        user = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "email": fake.email(),
        }
        fake_users.append(user)
    return fake_users


# region faker product


def generate_fake_product(
    nbr_product: int = NBR_PRODUCTS, nbr_spetech: int = NBR_SPETECH
) -> list[dict[str, str]]:
    """
    Generate fake product data using the Faker library.

    Args:
        nbr_product (int): The number of fake products to generate.
        nbr_spetech (int): The number of fake specifications to generate.

    Returns:
        list: A list of dictionaries containing fake product data.
    """
    fake = fk.Faker()
    fake_products = []
    for _ in range(nbr_product):
        product = {
            "product_name": fake.word(),
            "product_description": fake.text(),
            "price": f"{fake.pyint()}€",
            "picture": fake.url(),
            "spetech_id": fake.pyint(1, nbr_spetech),
        }
        fake_products.append(product)
    return fake_products


# region faker order


def generate_fake_orderhead(
    nbr_orders: int = NBR_ORDERS, nbr_user: int = NBR_USERS
) -> list[dict[str, str]]:
    """
    Generate fake order data using the Faker library.

    Args:
        nbr_orders (int): The number of fake orders to generate.
        nbr_user (int): The number of fake users to generate.

    Returns:
        list: A list of dictionaries containing fake order data.
    """
    fake = fk.Faker()
    fake_orders = []
    for _ in range(nbr_orders):
        order = {
            "orderhead_date": fake.date(),
            "user_id": fake.pyint(1, nbr_user),
        }
        fake_orders.append(order)
    return fake_orders


# region faker spetech


def generate_fake_spetech(nbr_spetech: int = NBR_SPETECH) -> list[dict[str, str]]:
    """
    Generate fake specifications data using the Faker library.

    Args:
        nbr_spetech (int): The number of fake specifications to generate.

    Returns:
        list: A list of dictionaries containing fake specifications data.
    """
    fake = fk.Faker()
    fake_spetech = []
    frame_sizes = ["S", "M", "L", "XL"]
    for _ in range(nbr_spetech):
        spetech = {
            "spetech_type": fake.name(),
            "color": fake.color(),
            "spetech_weight": fake.pyfloat(),
            "brand": fake.company(),
            "frame_size": frame_sizes[fake.pyint(0, len(frame_sizes) - 1)],
        }
        fake_spetech.append(spetech)
    return fake_spetech


# region fake orderdetai


def generate_fake_orderdetail(
    nbr_orderdetail: int = NBR_ORDERDETAIL,
    nbr_order: int = NBR_ORDERS,
    nbr_product: int = NBR_PRODUCTS,
) -> list[dict[str, str]]:
    """
    Generate fake specifications data using the Faker library.

    Args:
        nbr_spetech (int): The number of fake specifications to generate.

    Returns:
        list: A list of dictionaries containing fake specifications data.
    """
    fake = fk.Faker()
    fake_orderdetail = []

    for _ in range(nbr_orderdetail):
        orderdetail = {
            "product_id": fake.pyint(1, nbr_order),
            "orderhead_id": fake.pyint(1, nbr_product),
        }
        fake_orderdetail.append(orderdetail)
    return fake_orderdetail
