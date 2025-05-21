from src.db_api import DBConnection

ma_connexion = DBConnection('online_bikes.db')
ma_connexion.executescript('src/db.sql')
mon_enreg = ma_connexion.new_table_record('Product', {'product_Id' : 2}, False)
mon_enreg.set_field('description', 'voici ma nouvelle description.')
mon_enreg.save_record()

mon_enreg = ma_connexion.new_table_record('Product', {'product_Id' : None}, True)
mon_enreg.set_field('description', 'Ceci est un nouveau produit.')
mon_enreg.set_field('price', 123)
mon_enreg.save_record()

ma_connexion.delete_record('Product', {'product_Id' : 2})

ma_connexion.commit()