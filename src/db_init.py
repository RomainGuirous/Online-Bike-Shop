# from pymongo import MongoClient
from utils import (
    generate_fake_user,
    generate_fake_product,
    generate_fake_orderhead,
    generate_fake_spetech,
)
from products.models import Product
from spetech.models import SpeTech
from users.models import User
from users.utils import update_auth_config_from_users
from orders.models import OrderHead
from db_api import create_connection, ConnectionType
from random import randint

conn = create_connection()
if conn.is_of_type(ConnectionType.SQLITE):
    conn.executescript("src/db.sql")

# liste des dico
user_data = generate_fake_user()
product_data = generate_fake_product()
orderhead_data = generate_fake_orderhead()
spetech_data = generate_fake_spetech()

user_ids = []
spetech_ids = []
product_ids = []


def random_element_list(liste_elmt: list) -> any:
    return liste_elmt[randint(0, len(liste_elmt) - 1)]


# injection products
for spetech_dico in spetech_data:
    spetech = SpeTech(conn, is_new=True)
    spetech.color = spetech_dico["color"]
    spetech.brand = spetech_dico["brand"]
    spetech.spetech_weight = spetech_dico["spetech_weight"]
    spetech.spetech_type = spetech_dico["spetech_type"]
    spetech.frame_size = spetech_dico["frame_size"]

    spetech.save_to_db()
    spetech_ids.append(spetech.spetech_id)


# injection products
for product_dico in product_data:
    product = Product(conn, is_new=True)
    product.product_name = product_dico["product_name"]
    product.product_description = product_dico["product_description"]
    product.price = product_dico["price"]
    product.picture = product_dico["picture"]
    product.spetech_id = random_element_list(spetech_ids)

    product.save_to_db()
    product_ids.append(product.product_id)


# injection users

# first, we create a user used to connect to the shop...
user = User(conn, is_new=True)
user.first_name = "John"
user.last_name = "Smith"
user.email = "john.smith@test.com"
user.username = "jsmith"
user.is_admin = True
user.hashed_password = "123"
user.password_hint = "A very simple number..."
user.save_to_db()
user_ids.append(user.user_id)

for user_dico in user_data:
    user = User(conn, is_new=True)
    user.first_name = user_dico["first_name"]
    user.last_name = user_dico["last_name"]
    user.email = user_dico["email"]
    user.username = user_dico["username"]
    user.is_admin = user_dico["is_admin"]
    user.hashed_password = user_dico["hashed_password"]
    user.password_hint = user_dico["password_hint"]
    user.save_to_db()
    user_ids.append(user.user_id)


# injection orderheads
for orderhead_dico in orderhead_data:
    orderhead = OrderHead(conn, True)
    orderhead.user_id = random_element_list(user_ids)
    orderhead.orderhead_date = orderhead_dico["orderhead_date"]
    if conn.is_of_type(ConnectionType.SQLITE):
        orderhead.save_to_db()
    orderhead.add_product(random_element_list(product_ids), randint(1, 3))
    orderhead.save_to_db()

conn.commit()
# we generate config.yaml for connections rights
update_auth_config_from_users(conn)
