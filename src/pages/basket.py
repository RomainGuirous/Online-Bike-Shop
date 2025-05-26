import streamlit as st
from streamlit_card import card
from db_api import create_connection
from products.models import Product
import streamlit_utils as st_utils

connection = create_connection()
basket = st_utils.get_session_basket()

st.set_page_config(page_title="Basket", page_icon="🛒")
st_utils.hide_sidebar_pages()
st_utils.show_global_menu()

st_utils.handle_access_rights("user", "Please sign in to access your basket.")


if st.session_state.get("product_to_add_to_basket", None) is not None:
    basket.add(st.session_state["product_to_add_to_basket"], 1)
    del st.session_state["product_to_add_to_basket"]

if len(basket.get_product_list()) == 0:
    st.error("Your basket is empty.")
else:
    cols = st.columns(2)
    product_id_list = basket.get_product_list()
    for product_index in range(len(product_id_list)):
        with cols[product_index % 2]:
            product = Product(connection, False, product_id_list[product_index])
            card(
                title=product.product_name,
                text=product.product_description,
                image=product.picture,
            )
            col_qt_less, col_qt, col_qt_plus = st.columns(3)
            qt = basket.get_quantity(product.product_id)
            with col_qt_less:
                if qt == 1:
                    caption = '🗑️'
                else:
                    caption = '➖'
                if st.button(label=caption, key='qt-' + str(product.product_id)):
                    basket.add(product.product_id, -1)
                    st.switch_page('pages/basket.py')
            with col_qt:
                st.text(basket.get_quantity(product.product_id))
            with col_qt_plus:
                if st.button(label='➕', key='qt+' + str(product.product_id)):
                    basket.add(product.product_id, 1)
                    st.switch_page('pages/basket.py')
if st.button("Order now"):
    connection = create_connection()
    basket.create_order(connection, 8)
    connection.commit()
    st.switch_page("pages/orders.py")
