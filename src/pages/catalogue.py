import streamlit as st
from streamlit_card import card
from products.utils import get_product_list
from db_api import DBConnection
from img import liste_img

st.set_page_config(
    page_title="Catalogue",
    page_icon="📚",
)

conn = DBConnection("online_bikes.db")
if conn:
    list_data_product = get_product_list(conn)


cols = st.columns(2)

for i in range(len(list_data_product)):
    with cols[i % 2]:
        card(
            title=list_data_product[i]["product_name"],
            text=list_data_product[i]["product_description"],
            image=liste_img[i],
            on_click=lambda: st.switch_page("pages/connection.py"),
            styles={
                "card": {
                    "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
                },
                "filter": {
                    "background-color": "transparent",
                },
            },
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
