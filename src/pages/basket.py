import streamlit as st
from streamlit_card import card
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
from db_api import DBConnection
from basket import Basket
from products.models import Product

st.set_page_config(page_title="Catalogue", page_icon="🛒")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

if "user" not in (st.session_state.get("roles") or []):
    st.error("you must be logged in to access this page.")
    
    if st.button("Login"):
        st.switch_page("pages/connection.py")
    st.stop()
    
if st.session_state.get('authentication_status'):
    st.success(f'Welcome {st.session_state["name"]}!')
    authenticator.logout()

if st.session_state.get('basket'):
    basket: Basket = st.session_state["basket"]
else:
    basket = Basket()
    st.session_state["basket"] = basket

if st.session_state.get('connection'):
    connection: DBConnection = st.session_state["connection"]
else:
    connection = DBConnection()
    st.session_state["connection"] = connection

if len(basket.get_product_list()) == 0:
    st.error("Your basket is empty.")
else:
    cols = st.columns(2)
    for product_index in range(basket.get_product_list()):
        with cols[product_index % 2]:
            product_id = basket.get_product_list(product_index)
            product = Product(connection, False, product_id)
            card(
                title=f"({product.product_id}) {product.product_name} QT = {basket.get_quantity(product_id)}",
                text=product.product_description,
                image=product.picture,
                #on_click=lambda: st.switch_page("pages/connection.py"),
            )