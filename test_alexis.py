import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from src.db_api import create_connection
from src.users.utils import update_auth_config_from_users

connection = create_connection()

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

update_auth_config_from_users(connection)