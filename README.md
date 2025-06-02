# Online-Bike-Shop

Bienvenue sur **Online-Bike-Shop**!
Online-Bike-Shop est une application web interactive qui permet de gérer un catalogue de vélos, de consulter des fiches produits détaillées, d’ajouter des articles à un panier et de simuler des achats en ligne.
Le projet propose également une interface d’administration pour la gestion des produits et des commandes. Il est conçu pour fonctionner aussi bien avec une base de données SQLite qu’avec MongoDB, offrant ainsi une flexibilité d’utilisation autour de deux technologies de stockage.
L’interface, développée avec Streamlit, est responsive et personnalisable, adaptée à tous les supports.

## Fonctionnalités

- 🛒 Catalogue de vélos avec affichage par cartes
- 🔍 Fiche produit détaillée
- ➕ Ajout au panier
- 🧺 Gestion du panier
- 🛠️ Pages d’administration (gestion des produits, etc.)
- 🔑 Connexion utilisateur
- 📱 Interface responsive et personnalisée

## Structure du projet

```
Online-Bike-Shop/
│
├── src/                       # Code source principal
│   ├── main.py                # Page d'accueil Streamlit
│   ├── db_api.py              # Accès base de données SQLite/MongoDB
│   ├── config.py              # Configuration globale
│   ├── products/              # Modèles et utilitaires produits
│   ├── orders/                # Modèles et utilitaires commandes
│   ├── users/                 # Modèles utilisateurs
│   ├── spetech/               # Spécificités techniques vélos
│   ├── style/                 # Styles CSS personnalisés
│   ├── streamlit_utils.py     # Fonctions utilitaires Streamlit
│   └── pages/                 # Pages Streamlit (catalogue, panier, etc.)
│
├── online_bikes.db            # Base de données SQLite (si utilisée)
├── requirements.txt           # Dépendances Python
├── test_class_db.py           # Script de test de la base de données
├── .env                       # Configuration (choix SQL/MongoDB)
└── README.md                  # Ce fichier
```

## Installation

1. **Cloner le dépôt**
```sh
git clone git@github.com:RomainGuirous/Online-Bike-Shop.git
```
2. **Créer un environnement virtuel**
```sh
python3 -m venv .venv
source .venv/bin/activate
```
3. **Installer les dépendances**
```sh
pip install -r requirements.txt
```
4. **Configurer la base de données**
- Par défaut, l’application fonctionne avec *SQLite* (`online_bikes.db`).
- Pour utiliser MongoDB, créez simplement un fichier `.env` à la racine du projet avec la ligne suivante :
```sh
CONNECTION_TYPE=nosql
```
- Pour revenir à SQLite, mettez dans le `.env` :
```sh
CONNECTION_TYPE=sql
```
- Vérifiez et adaptez les paramètres selon votre environnement (voir `src/config.py` pour les détails).
5. **Lancer l’application**
```sh
streamlit run src/main.py
```

## Contribuer
Les contributions sont les bienvenues !
Merci de créer une issue ou une pull request pour toute suggestion ou amélioration.

## Auteurs  
Projet réalisé par FA, AH, RG. 