import streamlit as st
from db_api import DBConnection
from products.utils import get_product_list, get_spetech_list
from streamlit import session_state as st_session

st.set_page_config(
    page_title="Product",
    page_icon="🚲",
)

css = """
    <style>
        .stApp {
            background-image: url("https://bikes.com/cdn/shop/files/RM_MY25_NewColours_Altitude_Opt2.jpg?v=1738878523&width=2880");
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


if "id" not in st_session:
    st.session_state["id"] = None
elif st.session_state["id"]:
    st.write(st.session_state["id"])
    conn = DBConnection("online_bikes.db")
    if conn:
        list_data_product = get_product_list(conn)
        list_data_spetech = get_spetech_list(conn)

    product = list_data_product[st.session_state["id"] - 1]
    spetech = list_data_spetech[product["spetech"] - 1]

    css_product = (
        f'<span style="color:orange">{product["product_name"].capitalize()}</span>'
    )

    # st.write(product)
    # st.write(list_data_spetech)

    st.markdown(
        f'<span style="color:chartreuse">{product["product_name"].capitalize()}</span>',
        unsafe_allow_html=True,
    )
    st.image(product["picture"])
    st.write(product["product_description"])
    st.write(f"Price : {product['price']}")
    for key, value in spetech.items():
        if key != "spetech_id":
            if key == "spetech_type":
                st.write(f"Type : {value}")
            elif key == "spetech_weight":
                st.write(f"Weight : {value}")
            elif key == "frame_size":
                st.write(f"Frame Size : {value}")
            else:
                st.write(f"{key.capitalize()} : {value}")

    st.session_state["id"] = None
