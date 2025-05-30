from pymongo import MongoClient
from utils import (
    generate_fake_user,
    generate_fake_product,
    generate_fake_orderhead,
    generate_fake_spetech,
    generate_fake_orderdetail,
)

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["Online_Bike_Shop"]

# liste des dico (lignes)
user_data = generate_fake_user()
product_data = generate_fake_product()
orderhead_data = generate_fake_orderhead()
spetech_data = generate_fake_spetech()
orderdetail_data = generate_fake_orderdetail()


# Création (ou accès) des collections
product_collection = db["products"]
user_collection = db["user"]
spetech_collection = db["spetech"]
orderhead_collection = db["orderhead"]
orderdetail_collection = db["orderdetail"]

# injection des data en DB Mongo
list_collections = ["Product", "User", "SpeTech", "OrderHead", "OrderDetailx"]
for collection in list_collections:
    locals()[f"{collection}_collection"].insert_many(locals()[f"{collection}_data"])
