from src.db_api import DBConnection
#from src.users.models import User
from src.orders.models import OrderHead, OrderDetail

from src.utils import (
    generate_fake_orderhead,
    generate_fake_product,
    generate_fake_user,
    generate_fake_spetech,
    generate_fake_orderdetail,
)

ma_connexion = DBConnection("online_bikes.db")

def injection_faker(table: str, liste_fake_datas: list[dict[str, any]]) -> None:
    """
    Inject fake data into the specified table.

    Args:
        table (str): The name of the table to inject data into.
        liste_fake_datas (list[dict[str, any]]): A list of dictionaries containing fake data.

    Returns:
        None
    """

    for data in liste_fake_datas:
        mon_enreg = ma_connexion.new_table_record(
            table, {f"{table.lower()}_id": None}, True
        )
        for key, value in data.items():
            mon_enreg.set_field(key, value)
        mon_enreg.save_record()

ma_connexion.executescript("src/db.sql")

# product_data = generate_fake_product()
# order_data = generate_fake_orderhead()
# user_data = generate_fake_user()
# spetech_data = generate_fake_spetech()
# orderdetail_data = generate_fake_orderdetail()
# injection_faker("User", user_data)
# injection_faker("Product", product_data)
# injection_faker("Orderhead", order_data)
# injection_faker("SpeTech", spetech_data)

# ajout d'une commande
commande = OrderHead(ma_connexion, True)
commande.user_id = 8
commande.orderhead_date = '2025-05-21'
commande.save_to_db()
ma_connexion.commit()
commande.add_product(3, 5) # on ajoute le produit 3 avec une qt de 5
commande.add_product(1, 5)
commande.add_product(2, 2)
commande.save_to_db()
ma_connexion.commit()
num_commande = commande.orderhead_id
print(f"Commande enregistrée avec le N° {num_commande}")
for detail in commande.details():
    print(f"  Produit : {detail.product_id} Qt : {detail.quantity}")

input("Vérifier en base la création de la commande et des lignes...")
# on supprime le détail n°2 (correspondant au produit 1) et on re-enregistre...
del commande.details()[1]
commande.save_to_db()
ma_connexion.commit()
input("Vérifier en base la suppression du produit 1...")
# on recharge... et on affiche les lignes
commande = OrderHead(ma_connexion, False, num_commande)
for detail in commande.details():
    print(f"  Produit : {detail.product_id} Qt : {detail.quantity}")
ma_connexion.commit()
