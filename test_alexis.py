import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from src.db_api import create_connection

# nouveau_produit = connection.get_record_object('Product', None, True)
# nouveau_produit.set_field('product_name', 'toto')
# nouveau_produit.save()
# id_produit = nouveau_produit.get_field('_id')
# print(f"ID du produit : {id_produit}")

# produit_existant = connection.get_record_object('Product', id_produit, False)
# produit_existant.set_field('price', 123)
# produit_existant.save()
# print(f"ID du produit : {produit_existant.get_field('_id')}")
# print(f"Nom = {produit_existant.get_field('product_name')} Prix = {produit_existant.get_field('price')}")

db_connection = create_connection()

# If using NoSQL, fetch best-selling products from the collection
products_list = db_connection.new_query()["OrderHead"].find()
product_sales = {}
for order in products_list:
    for detail in order["OrderDetails"]:
        product_id = detail.get("product_id")
        quantity = detail.get("quantity", 0)
        if product_id in product_sales:
            product_sales[product_id] += quantity
        else:
            product_sales[product_id] = quantity

# Sort products by total quantity sold and get the top 4
sorted_products = sorted(product_sales.items(), key=lambda x: x[1], reverse=True)[:4]
product_ids = [product[0] for product in sorted_products]

# Fetch product details for the top products
products = db_connection.new_query()["Product"].find({"_id": {"$in": product_ids}})
print([product for product in products if product["_id"] in product_ids])
print([product for product in products if product["_id"] in product_ids])

db_connection.commit()

# update_auth_config_from_users(connection)
