from src.db_api import DBConnection

from src.utils import (
    generate_fake_orderhead,
    generate_fake_product,
    generate_fake_user,
    generate_fake_spetech,
    generate_fake_orderdetail,
)

product_data = generate_fake_product()
order_data = generate_fake_orderhead()
user_data = generate_fake_user()
spetech_data = generate_fake_spetech()
orderdetail_data = generate_fake_orderdetail()

ma_connexion = DBConnection("online_bikes.db")
ma_connexion.executescript("src/db.sql")


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


#injection_faker("User", user_data)
#injection_faker("Product", product_data)
#injection_faker("Orderhead", order_data)
#injection_faker("SpeTech", spetech_data)
# mon_enreg = ma_connexion.new_table_record("Product", {"product_Id": "AUTO"}, True)
# mon_enreg.set_field("description", "voici ma nouvelle description.")
# mon_enreg.save_record()

# mon_enreg = ma_connexion.new_table_record("Product", {"product_Id": "AUTO"}, True)
# mon_enreg.set_field("description", "Ceci est un nouveau produit.")
# mon_enreg.set_field("price", 123)
# mon_enreg.save_record()


# ma_connexion.delete_record('Product', {'product_Id' : 1})