# main application logic, launch streamlit app, etc.
import streamlit as st

from streamlit import session_state as st_session
from streamlit_card import card
from products.utils import get_product_list
from db_api import DBConnection
from config import DB_FILE


st.set_page_config(
    page_title="Page d'accueil",
    page_icon="🚴",
)


def main():

    css = '''
    <style>
        .stApp {
            background-image: url("https://www.les3vallees.com/media/cache/hero_single/ete-vtt-et-vae-addict-tribu-meribel-1920x1080-arthur-bertrand-293.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .stApp > header {       
            background-color: transparent;
        }
    </style>
    '''

    st.markdown(css, unsafe_allow_html=True)

    #initialize session state
    if "connection" not in st_session:
        st_session["connection"] = None
        
    if "role" not in st_session:
        st_session["role"] = "default"  # Default role


    conn = DBConnection(DB_FILE)
    st_session["connection"] = conn
    
    if conn:
        products = get_product_list(conn)
    else:
        st.error("Database connection failed.")
        st.stop()

    cols = st.columns(2)
    # Example of adding bike data

    if products:
        for i in range(len(products)):
            with cols[i % 2]:
                card(
                    title=products[i]['name'],
                    text=products[i]['description'],
                    image=products[i]['picture'],
                    on_click=lambda: st.switch_page("pages/connection.py"),
                    styles={
                        "card": {
                            "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",

                        },
                        "filter": {
                            "background-color": "transparent",
                            
                        },
                    },
                )
    else:
        st.write("No products found.")

# Product details
product = {
    "title": "X-Trail Carbon Mountain Bike",
    "price": "$749.00",
    "image": "https://cyclelimited.com/cdn/shop/files/A99A8160_2560x2560.jpg?v=1699641023",  # Replace with your actual product image
    "link": "https://www.yourbikeshop.com/xtrail-500"
}

# HTML for modern product card
card_html = f"""
<style>
.product-card {{
    background-color: #ffffff;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    padding: 20px;
    width: 300px;
    text-align: center;
    font-family: 'Segoe UI', sans-serif;
    margin: auto;
}}

.product-card img {{
    width: 100%;
    border-radius: 8px;
    margin-bottom: 16px;
}}

.product-title {{
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 8px;
}}

.product-price {{
    font-size: 18px;
    color: #b12704;
    margin-bottom: 16px;
}}

.product-button {{
    background-color: #111;
    color: #fff;
    padding: 10px 18px;
    border: none;
    border-radius: 6px;
    text-decoration: none;
    font-size: 15px;
    font-weight: 500;
    transition: background-color 0.3s ease;
    display: inline-block;
}}

.product-button:hover {{
    background-color: #333;
}}
</style>

<div class="product-card">
    <img src="{product['image']}" alt="Bike Image">
    <div class="product-title">{product['title']}</div>
    <div class="product-price">{product['price']}</div>
    <a href="{product['link']}" class="product-button" target="_blank">Add to Cart</a>
</div>
"""

# Render the card
st.markdown(card_html, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
