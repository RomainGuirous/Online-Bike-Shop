# utility functions for the application
# database import

import faker as fk
from config import (
    NBR_USERS,
    NBR_PRODUCTS,
    NBR_SPETECH,
    NBR_ORDERS,
    NBR_ORDERDETAIL,
)
from img import liste_img

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
            "is_admin": False,
            "hashed_password": fake.password(5),
            "password_hint": fake.sentence(4),
        }
        user["email"] = (
            user["first_name"] + "." + user["last_name"] + "@example.com"
        ).lower()
        user["username"] = (user["first_name"] + "." + user["last_name"]).lower()
        fake_users.append(user)
    return fake_users


# region faker product


def generate_fake_product(
    nbr_product: int = NBR_PRODUCTS, nbr_spetech: int = NBR_SPETECH, mongo: bool = False
) -> list[dict[str, str]]:
    """
    Generate fake product data using the Faker library.

    Args:
        nbr_product (int): The number of fake products to generate.
        nbr_spetech (int): The number of fake specifications to generate.
        mongo (bool): If True, the function will not include spetech_id in the product data.

    Returns:
        list: A list of dictionaries containing fake product data.
    """
    if len(liste_img) < nbr_product:
        raise ValueError("Il n'y a pas assez d'images pour les produits.")
    fake = fk.Faker()
    fake_products = []
    for i in range(nbr_product):
        product = {
            "product_name": fake.word(),
            "product_description": fake.text(),
            "price": fake.pyint(),
            "picture": liste_img[i],
        }
        if not mongo:
            spetech_id = fake.pyint(1, nbr_spetech)
            product["spetech_id"] = spetech_id

        fake_products.append(product)
    return fake_products


# region faker order


def generate_fake_orderhead(
    nbr_orders: int = NBR_ORDERS, nbr_user: int = NBR_USERS, mongo: bool = False
) -> list[dict[str, str]]:
    """
    Generate fake order data using the Faker library.

    Args:
        nbr_orders (int): The number of fake orders to generate.
        nbr_user (int): The number of fake users to generate.
        mongo (bool): If True, the function will not include user_id in the order data.

    Returns:
        list: A list of dictionaries containing fake order data.
    """
    fake = fk.Faker()
    fake_orders = []
    for _ in range(nbr_orders):
        order = {
            "orderhead_date": fake.date(),
        }
        if not mongo:
            user_id = fake.pyint(1, nbr_user)
            order["user_id"] = user_id

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
            "color": fake.color_name(),
            "spetech_weight": fake.pyfloat(
                right_digits=fake.pyint(0, 2),  # entre 0 et 2 chiffres après la virugle
                positive=True,
                min_value=1,
                max_value=100,
            ),
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
