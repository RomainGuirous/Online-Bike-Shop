from src.db_api import create_connection

connection = create_connection()

nouveau_produit = connection.get_record_object('Product', None, True)
nouveau_produit.set_field('product_name', 'toto')
nouveau_produit.save()
id_produit = nouveau_produit.get_field('_id')
print(f"ID du produit : {id_produit}")

produit_existant = connection.get_record_object('Product', id_produit, False)
produit_existant.set_field('price', 123)
produit_existant.save()
print(f"ID du produit : {produit_existant.get_field('_id')}")
print(f"Nom = {produit_existant.get_field('product_name')} Prix = {produit_existant.get_field('price')}")