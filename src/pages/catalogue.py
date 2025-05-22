import streamlit as st
from streamlit_card import card
from products.utils import get_product_list
from db_api import DBConnection

st.set_page_config(
    page_title="Catalogue",
    page_icon="📚",
)

css = """
    <style>
        .stApp {
            background-image: url("https://wallpapers.com/images/hd/sunset-sky-background-92b7gfssbwa36cle.jpg");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .stApp > header {       
            background-color: transparent;
        }
    </style>
    """

st.markdown(css, unsafe_allow_html=True)


conn = DBConnection("online_bikes.db")
if conn:
    list_data_product = get_product_list(conn)


def click(id: int):
    st.session_state["id"] = list_data_product[id]["product_id"]
    st.switch_page("pages/product.py")


cols = st.columns(2)

for i in range(len(list_data_product)):
    with cols[i % 2]:
        card(
            title=list_data_product[i]["product_name"],
            text=list_data_product[i]["product_description"],
            image=list_data_product[i]["picture"],
            on_click=lambda: click(i),
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
