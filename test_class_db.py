from src.db_api import DBConnection
from src.users.schemas import User

ma_connexion = DBConnection('online_bikes.db')
#ma_connexion.executescript('src/db.sql')
#mon_enreg = ma_connexion.new_table_record('Product', {'product_Id' : 2}, False)
#mon_enreg.set_field('description', 'voici ma nouvelle description.')
#mon_enreg.save_record()
#mon_enreg = ma_connexion.new_table_record('Product', {'product_Id' : None}, True)
#mon_enreg.set_field('description', 'Ceci est un nouveau produit.')
#mon_enreg.set_field('price', 123)
#mon_enreg.save_record()
#ma_connexion.delete_record('Product', {'product_Id' : 2})

mon_nouvel_utilisateur = User(ma_connexion, True)
mon_nouvel_utilisateur.first_name = 'Toto'
mon_nouvel_utilisateur.last_name = 'AZERTY'
mon_nouvel_utilisateur.save_to_db()
ma_connexion.commit()