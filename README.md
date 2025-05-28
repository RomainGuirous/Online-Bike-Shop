# Online-Bike-Shop

Bienvenue sur **Online-Bike-Shop**, une application web de démonstration pour la gestion et la vente de vélos en ligne, réalisée avec [Streamlit](https://streamlit.io/) et SQLite.

## Fonctionnalités

- Catalogue de vélos avec affichage par cartes
- Fiche produit détaillée
- Ajout au panier
- Gestion du panier
- Pages d’administration (gestion des produits, etc.)
- Connexion utilisateur (bientôt)
- Interface responsive et personnalisée

## Structure du projet

```
Online-Bike-Shop/
│
├── src/                  # Code source principal
│   ├── main.py           # Page d'accueil Streamlit
│   ├── db_api.py         # Accès base de données SQLite
│   ├── config.py         # Configuration
│   ├── products/         # Modèles et utilitaires produits
│   ├── orders/           # Modèles et utilitaires commandes
│   ├── users/            # Modèles utilisateurs
│   ├── spetech/          # Spécificités techniques vélos
│   ├── style/            # Styles CSS personnalisés
│   ├── streamlit_utils.py# Fonctions utilitaires Streamlit
│   └── pages/            # Pages Streamlit (catalogue, panier, etc.)
│
├── [online_bikes.db]      # Base de données SQLite
├── [requirements.txt]     # Dépendances Python
├── [test_class_db.py]     # Script de test de la base de données
└── [README.md]            # Ce fichier
```


## Installation

1. **Cloner le dépôt**
```sh
git clone git@github.com:RomainGuirous/Online-Bike-Shop.git
```
2. **Créer un environnement virtuel**

python3 -m venv .venv
source .venv/bin/activate

3. **Installer les dépendances**

pip install -r requirements.txt

4. **Lancer l’application**

streamlit run src/main.py

## Contribuer
Les contributions sont les bienvenues !
Merci de créer une issue ou une pull request pour toute suggestion ou amélioration.

## Auteurs
Projet réalisé par FA, AH, RG. 