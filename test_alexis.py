from src.db_api import create_connection, DBDocument
from pymongo.database import Database

connection = create_connection()

nouveau_document = DBDocument(connection, 'Product', None)
nouveau_document.set_field('product_name', 'toto')
nouveau_document.save_document()
id_produit = nouveau_document.get_field('_id')
print(f"ID du produit : {id_produit}")

produit_existant = DBDocument(connection, 'Product', id_produit)
produit_existant.set_field('price', 123)
produit_existant.save_document()
print(f"ID du produit : {produit_existant.get_field('_id')}")
print(f"Nom = {produit_existant.get_field('product_name')} Prix = {produit_existant.get_field('price')}")