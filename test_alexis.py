import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from src.db_api import create_connection, ConnectionType
from orders.models import OrderHead

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

commande = OrderHead(db_connection, True)
commande.user_id = 8
commande.orderhead_date = "2025-05-21"
if db_connection.is_of_type(ConnectionType.SQLITE):
    commande.save_to_db()
commande.add_product(3, 5)  # on ajoute le produit 3 avec une qt de 5
commande.add_product(1, 5)
commande.add_product(2, 2)
commande.save_to_db()

db_connection.commit()

# update_auth_config_from_users(connection)
