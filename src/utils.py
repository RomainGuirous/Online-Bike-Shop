# utility functions for the application
# add bike data to the database

from database import create_connection, close_connection
from config import DB_FILE
import faker as fk

# region add data


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
        print("Failed to add bike data.")


# region faker user


def generate_fake_user(nbr_users: int) -> list[dict[str, str]]:
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
            "first_name": fake.name(),
            "last_name": fake.name(),
            "email": fake.email(),
        }
        fake_users.append(user)
    return fake_users


# region faker product


def generate_fake_product(nbr_product: int, nbr_spetech: int) -> list[dict[str, str]]:
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
            "product_name": fake.space_object_name(),
            "description": fake.text(),
            "price": fake.pyint() + "€",
            "picture": fake.url(),
            "septech_id": fake.pyint(1, nbr_spetech),
        }
        fake_products.append(product)
    return fake_products


# region faker order


def generate_fake_order(nbr_orders: int, nbr_user: int) -> list[dict[str, str]]:
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
            "date": fake.date(),
            "quantity": fake.pyint(),
            "user_informations": fake.text(),
            "user_id": fake.pyint(1, nbr_user),
        }
        fake_orders.append(order)
    return fake_orders


# region faker spetech


def generate_fake_spetech(nbr_spetech: int) -> list[dict[str, str]]:
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
            "type": fake.name(),
            "color": fake.color(),
            "weight": fake.pyfloat(),
            "brand": fake.company(),
            "frame_size": frame_sizes[fake.pyint(0, len(frame_sizes) - 1)],
        }
        fake_spetech.append(spetech)
    return fake_spetech
