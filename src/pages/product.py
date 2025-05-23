import streamlit as st
from db_api import create_connection
from streamlit import session_state as st_session
from streamlit_card import card
import streamlit_utils as st_utils
from products.models import Product
from spetech.models import SpeTech

connection = create_connection()

st.set_page_config(page_title="Product", page_icon="🚲")
st_utils.show_global_menu()

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
    product = Product(connection, False, st.session_state["id"])
    spetech = None
    if product.spetech_id > 0:
        spetech = SpeTech(connection, False, product.spetech_id)

    def text_field_color(field: str, color: str) -> None:
        return st.markdown(
            f'<span style="color:{color}">{field.capitalize()}</span>',
            unsafe_allow_html=True,
        )

    # text_field_color(product.product_name, "chartreuse")
    st.image(product.picture)
    # st.write(product.product_description)
    # st.write(f"Price : {product.price}")
    # if spetech is not None:
    #     if spetech.spetech_type:
    #         st.write(f"Type : {spetech.spetech_type}")
    #     if spetech.spetech_weight:
    #         st.write(f"Weight : {spetech.spetech_weight}")
    #     if spetech.frame_size:
    #         st.write(f"Frame Size : {spetech.frame_size}")

    css_card = f"""
    <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
        <h1>{product.product_name.capitalize()}</h1>
        <p>{product.product_description}</p>
        <p><strong>Price: </strong>{product.price}</p>
        <p><strong>Brand: </strong>{spetech.brand}</p>
        <p><strong>Type :</strong>{spetech.spetech_type}</p>
        <p><strong>Weight :</strong>{spetech.spetech_weight}</p>
        <p><strong>Frame Size :</strong>{spetech.frame_size}</p>
    </div>
    """

    st.markdown(css_card, unsafe_allow_html=True)

    card(
        title="Add to basket " + str(product.product_id),
        text="",
        # image=product.picture,
        on_click=lambda: st_utils.event_add_to_basket(product.product_id),
    )
