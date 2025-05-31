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
if conn.connection_type == ConnectionType.SQLITE:
    conn.executescript('src/db.sql')

# Connect to MongoDB (default localhost:27017)
# client = MongoClient("mongodb://localhost:27017/")

# # Drop the database if it exists (for fresh start)
# client.drop_database("BikeShopDB")

# Create/use the database
# db = client["BikeShopDB"]


# liste des dico (lignes)
user_data = generate_fake_user()
product_data = generate_fake_product()
orderhead_data = generate_fake_orderhead()
spetech_data = generate_fake_spetech()


# Création (ou accès) des collections (tables)
# product_collection = db["Products"]
# user_collection = db["User"]
# spetech_collection = db["Spetech"]
# orderhead_collection = db["Orderhead"]

# injection des data en DB Mongo
# list_collections = ["user", "spetech", "product", "orderhead", "orderdetail"]
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
user.first_name = 'John'
user.last_name = 'Smith'
user.email = 'john.smith@test.com'
user.username = 'jsmith'
user.is_admin = True
user.hashed_password = '123'
user.password_hint = 'A very simple number...'
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
    if conn.connection_type == ConnectionType.SQLITE:
        orderhead.save_to_db()
    orderhead.add_product(random_element_list(product_ids), randint(1, 3))
    orderhead.save_to_db()

conn.commit()
# we generate config.yaml for connections rights
update_auth_config_from_users(conn)


# # Insert into Product
# product_collection.insert_many(
#     [
#         {
#             "product_id": 1,
#             "product_name": "Mountain Bike",
#             "product_description": "A rugged mountain bike for off-road adventures.",
#             "price": 499.99,
#             "picture": "https://www.serk.cc/wp-content/uploads/2022/10/DSCF2936.jpg",
#             "spetech_id": 1,
#         },
#         {
#             "product_id": 2,
#             "product_name": "Road Bike",
#             "product_description": "A lightweight road bike for speed and efficiency.",
#             "price": 799.99,
#             "picture": "https://www.serk.cc/wp-content/uploads/2022/10/DSCF4542-Edit.jpg",
#             "spetech_id": 2,
#         },
#         {
#             "product_id": 3,
#             "product_name": "Hybrid Bike",
#             "product_description": "A versatile hybrid bike for city and trail riding.",
#             "price": 599.99,
#             "picture": "https://www.serk.cc/wp-content/uploads/2019/07/A21_1920-300x200.jpg",
#             "spetech_id": 3,
#         },
#         {
#             "product_id": 4,
#             "product_name": "Electric Bike",
#             "product_description": "An electric bike for effortless commuting.",
#             "price": 1299.99,
#             "picture": "https://www.serk.cc/wp-content/uploads/2019/07/A10_1920-300x200.jpg",
#             "spetech_id": 4,
#         },
#         {
#             "product_id": 5,
#             "product_name": "Kids Bike",
#             "product_description": "A fun and safe bike for kids.",
#             "price": 199.99,
#             "picture": "https://www.serk.cc/wp-content/uploads/2019/07/a30M_side.jpg",
#             "spetech_id": 5,
#         },
#     ]
# )

# # Insert into OrderHead
# orderhead_collection.insert_many(
#     [
#         {"orderhead_id": 1, "orderhead_date": "2023-10-01", "user_id": 1},
#         {"orderhead_id": 2, "orderhead_date": "2023-10-02", "user_id": 2},
#         {"orderhead_id": 3, "orderhead_date": "2023-10-03", "user_id": 3},
#         {"orderhead_id": 4, "orderhead_date": "2023-10-04", "user_id": 4},
#         {"orderhead_id": 5, "orderhead_date": "2023-10-05", "user_id": 5},
#         {"orderhead_id": 6, "orderhead_date": "2023-10-06", "user_id": 1},
#         {"orderhead_id": 7, "orderhead_date": "2023-10-07", "user_id": 2},
#         {"orderhead_id": 8, "orderhead_date": "2023-10-08", "user_id": 3},
#         {"orderhead_id": 9, "orderhead_date": "2023-10-09", "user_id": 4},
#         {"orderhead_id": 10, "orderhead_date": "2023-10-10", "user_id": 5},
#     ]
# )

# # Insert into OrderDetail
# orderdetail_collection.insert_many(
#     [
#         {"orderhead_id": 1, "product_id": 1, "quantity": 2},
#         {"orderhead_id": 1, "product_id": 2, "quantity": 1},
#         {"orderhead_id": 2, "product_id": 3, "quantity": 1},
#         {"orderhead_id": 2, "product_id": 4, "quantity": 2},
#         {"orderhead_id": 3, "product_id": 5, "quantity": 1},
#         {"orderhead_id": 4, "product_id": 1, "quantity": 1},
#         {"orderhead_id": 5, "product_id": 2, "quantity": 3},
#         {"orderhead_id": 6, "product_id": 3, "quantity": 2},
#         {"orderhead_id": 7, "product_id": 4, "quantity": 1},
#         {"orderhead_id": 8, "product_id": 5, "quantity": 4},
#     ]
# )

# # Insert into SpeTech
# spetech_collection.insert_many(
#     [
#         {
#             "spetech_id": 1,
#             "spetech_type": "Bike",
#             "color": "Red",
#             "spetech_weight": 12.5,
#             "brand": "Speedster",
#             "frame_size": "M",
#         },
#         {
#             "spetech_id": 2,
#             "spetech_type": "Bike",
#             "color": "Blue",
#             "spetech_weight": 13.0,
#             "brand": "TrailBlazer",
#             "frame_size": "L",
#         },
#         {
#             "spetech_id": 3,
#             "spetech_type": "Bike",
#             "color": "Green",
#             "spetech_weight": 11.5,
#             "brand": "EcoRider",
#             "frame_size": "S",
#         },
#         {
#             "spetech_id": 4,
#             "spetech_type": "Bike",
#             "color": "Yellow",
#             "spetech_weight": 12.0,
#             "brand": "SunRider",
#             "frame_size": "M",
#         },
#         {
#             "spetech_id": 5,
#             "spetech_type": "Bike",
#             "color": "Black",
#             "spetech_weight": 14.0,
#             "brand": "NightRider",
#             "frame_size": "XL",
#         },
#         {
#             "spetech_id": 6,
#             "spetech_type": "Bike",
#             "color": "White",
#             "spetech_weight": 12.8,
#             "brand": "CloudRider",
#             "frame_size": "M",
#         },
#     ]
# )

# # Insert into User
# user_collection.insert_many(
#     [
#         {
#             "user_id": 1,
#             "username": "johndoe",
#             "password": "securepassword123",
#             "first_name": "John",
#             "last_name": "Doe",
#             "email": "johndoe@example.com",
#         },
#         {
#             "user_id": 2,
#             "username": "janedoe",
#             "password": "securepassword456",
#             "first_name": "Jane",
#             "last_name": "Doe",
#             "email": "janedoe@example.com",
#         },
#         {
#             "user_id": 3,
#             "username": "alice",
#             "password": "securepassword789",
#             "first_name": "Alice",
#             "last_name": "Wonderland",
#             "email": "alice@example.com",
#         },
#         {
#             "user_id": 4,
#             "username": "bob",
#             "password": "securepassword101",
#             "first_name": "Bob",
#             "last_name": "Builder",
#             "email": "bob@example.com",
#         },
#         {
#             "user_id": 5,
#             "username": "charlie",
#             "password": "securepassword202",
#             "first_name": "Charlie",
#             "last_name": "Brown",
#             "email": "charlie@example.com",
#         },
#     ]
# )
