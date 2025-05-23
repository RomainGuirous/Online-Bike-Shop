import streamlit as st
from products.utils import get_product_list
from main import get_product_card
from db_api import create_connection
import streamlit_utils as st_utils

st.set_page_config(
    page_title="Catalogue",
    layout="wide",
    page_icon="📚",
)
st_utils.show_global_menu()

# background image
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


conn = create_connection()
if conn:
    list_data_product = get_product_list(conn)


def click(id: int):
    st.session_state["id"] = list_data_product[id]["product_id"]
    st.switch_page("pages/product.py")


st.markdown(
    """
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
    """,
    unsafe_allow_html=True,
)

# for i in range(len(list_data_product)):
#     with cols[i % 2]:
#         card(
#             title=list_data_product[i]["product_name"],
#             text=list_data_product[i]["product_description"],
#             image=list_data_product[i]["picture"],
#             on_click=lambda: click(i),
#             styles={
#                 "card": {
#                     "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
#                 },
#                 "filter": {
#                     "background-color": "transparent",
#                 },
#             },
#         )

cols_per_row = 4

# for i in range(0, len(list_data_product), cols_per_row):
#     row = st.columns(cols_per_row)
#     for j in range(cols_per_row):
#         if i + j < len(list_data_product):
#             product = list_data_product[i + j]
#             with row[j]:
#                 st.markdown(get_product_card(product), unsafe_allow_html=True)
#                 if st.button(
#                     f"Voir {product['product_name'].capitalize()}",
#                     key=f"btn_{product['product_id']}",
#                 ):
#                     st.session_state["id"] = product["product_id"]
#                     st.switch_page("pages/product.py")

for i in range(0, len(list_data_product), cols_per_row):
    row = st.columns(cols_per_row)
    for j in range(cols_per_row):
        if i + j < len(list_data_product):
            product = list_data_product[i + j]
            with row[j]:
                st.markdown(get_product_card(product), unsafe_allow_html=True)
                # Le bouton juste sous la card, donc "dans" la card visuellement
                btn_style = """
                    <style>
                    div.stButton > button {
                        width: 100%;
                        margin-top: -12px;
                        border-radius: 4px;
                        background: #f6f6f6;
                        border: 1px solid #ccc;
                        color: #111;
                        font-size: 14px;
                        font-weight: 400;
                    }
                    </style>
                """
                st.markdown(btn_style, unsafe_allow_html=True)
                if st.button(
                    f"Voir {product['product_name'].capitalize()}",
                    key=f"btn_{product['product_id']}",
                ):
                    st.session_state["id"] = product["product_id"]
                    st.switch_page("pages/product.py")
