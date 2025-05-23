import streamlit as st
from streamlit_card import card
from db_api import create_connection
from products.models import Product
import streamlit_utils as st_utils

connection = create_connection()
basket = st_utils.get_session_basket()

st.set_page_config(page_title="Basket", page_icon="🛒")
st_utils.show_global_menu()

st_utils.handle_access_rights('user', 'Please sign in to access your basket.')


if st.session_state.get("product_to_add_to_basket", None) is not None:
    basket.add(st.session_state['product_to_add_to_basket'], 1)
    del st.session_state['product_to_add_to_basket']

if len(basket.get_product_list()) == 0:
    st.error("Your basket is empty.")
else:
    cols = st.columns(2)
    for product_index in range(len(basket.get_product_list())):
        with cols[product_index % 2]:
            product_id = basket.get_product_list()[product_index]
            product = Product(connection, False, product_id)
            card(
                title=f"({product.product_id}) {product.product_name} QT = {basket.get_quantity(product_id)}",
                text=product.product_description,
                image=product.picture,
                #on_click=lambda: st.switch_page("pages/connection.py"),
            )
    if st.button("Order now"):
        connection = create_connection()
        basket.create_order(connection, 8)
        connection.commit()
        st.switch_page("pages/orders.py")