# main application logic, launch streamlit app, etc.
import streamlit as st
from products.utils import get_product_list
from db_api import DBConnection
from config import DB_FILE


st.set_page_config(
    page_title="Page d'accueil",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚴",
)


def main():

    css = '''
    <style>
        .stApp {
            background-image: url("https://bikes.com/cdn/shop/files/RM_MY25_NewColours_Growler_Opt2.jpg?v=1738878774&width=2880");
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
    if "connection" not in st.session_state:
        st.session_state["connection"] = None

    if "role" not in st.session_state:
        st.session_state["role"] = "default"  # Default role

    conn = DBConnection(DB_FILE)
    st.session_state["connection"] = conn

    if conn:
        products = get_product_list(conn)
    else:
        st.error("Database connection failed.")
        st.stop()

    # HTML for a product card with wider image
    def get_product_card(product):
        return f"""
        <a href="" target="_blank" class="product-card-link">
            <div class="product-card-wide">
                <img src="{product['picture']}" alt="Bike Image">
                <div class="product-title">{product['name']}</div>
                <div class="product-price">{product['price']}</div>
                <div class="product-button">🛒 Add to Cart</div>
            </div>
        </a>
        """


    # Inject global styles
    st.markdown("""
        <style>
        
        .product-card-wide {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 16px;
            margin-bottom: 16px;
            width: 100%;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        
        .product-card-link {
            text-decoration: none !important;
            color: inherit;
            display: block;
        }
        
        .product-card-wide img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 16px;
            transition: transform 0.1s ease, box-shadow 0.2s ease;
        }

        .product-title {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .product-price {
            font-size: 16px;
            color: #b12704;
            margin-bottom: 16px;
        }
        
        .product-button {
            background-color: transparent;
            color: #111;
            padding: 8px 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            text-decoration: none !important;
            font-size: 14px;
            font-weight: 400;
            transition: all 0.2s ease;
            display: inline-block;
            cursor: pointer;
        }

        .product-button:hover {
            background-color: #f6f6f6;
            border-color: #999;
            text-decoration: none !important;
        }
        </style>
    """, unsafe_allow_html=True)
    
    # title
    st.markdown(
        """
        <h1 style="text-align: center; color: #FFFFFF;">Welcome to the Online Bike Shop</h1>
        <p style="text-align: center; color: #FFFFFF;">Best selling product.</p>
        """,
        unsafe_allow_html=True
    )
    
    # Display cards in a 4-column responsive layout
    cols_per_row = 4
    for i in range(0, len(products), cols_per_row):
        row = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(products):
                with row[j]:
                    st.markdown(get_product_card(products[i + j]), unsafe_allow_html=True)

if __name__ == "__main__":
    main()
