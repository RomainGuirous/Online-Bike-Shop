# main application logic, launch streamlit app, etc.
import streamlit as st
from streamlit import session_state as st_session
from streamlit_card import card
from products.models import Product
from database import create_connection, close_connection
from config import DB_FILE

st.set_page_config(
    page_title="Page d'accueil",
    # bike icon
    page_icon="🚴",
)


def main():
    if "romain" not in st_session:
        st_session["romain"] = "connected"

    conn = create_connection(DB_FILE)
    if conn:
        # Run your application logic here
        close_connection(conn)
    else:
        st.error("Failed to connect to the database.")
        st.stop()

    # Streamlit app layout and components go here
    st.title("Bike Rental Application")
    st.write("Welcome to the Bike Rental Application!")
    st.write("This is a simple application to manage bike rentals.")

    st.write(st_session["romain"])

    st.button("test", on_click=lambda: st_session.update(romain="test"))
    st.write(st_session["romain"])

    # Example of adding bike data

    cols = st.columns(2)
    
    for i in range(10):
        with cols[i % 2]:
            card(
                title="Bike" + str(i),
                text="This is a bike description.",
                image="https://via.placeholder.com/150",
                on_click=lambda: st.switch_page("pages/connection.py"),
                # styles={
                #     "card": {
                #         "width": "100%",
                #         "height": "100%",
                #         "border-radius": "10px",
                #         "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                #     },
                #     "title": {"font-size": "20px", "font-weight": "bold"},
                #     "text": {"font-size": "14px"},
                # },
            )


if __name__ == "__main__":
    main()
