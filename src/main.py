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

# get all products
conn = DBConnection("online_bikes.db")
if conn:
    products = get_product_list(conn)
    st.write(products)


def main():
    if "role" not in st_session:
        st_session["role"] = "default"  # Default role

    if conn not in st_session:
        st_session["conn"] = None
    else:
        st_session["conn"] = conn

    # conn = create_connection(DB_FILE)
    # if conn:
    #     # Run your application logic here
    #     close_connection(conn)
    # else:
    #     st.error("Failed to connect to the database.")
    #     st.stop()

    # Streamlit app layout and components go here
    st.write(st_session["role"])
    st.button("Get access", on_click=lambda: st_session.update(role="admin"))
    st.write(st_session["role"])

    # Example of adding bike data

    cols = st.columns(2)
    # Example of adding bike data

    print(products[0])

    for i in range(len(products)):
        with cols[i % 2]:
            card(
                title=products[i]["name"],
                text=products[i]["description"],
                image=products[i]["picture"],
                on_click=lambda: st.switch_page("pages/connection.py"),
            )


if __name__ == "__main__":
    main()
