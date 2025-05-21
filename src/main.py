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

# conn = st.connection(DB_FILE, type="sql")

def main():
    
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
    
if __name__ == "__main__":
    main()
