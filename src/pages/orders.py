import streamlit as st
from streamlit_card import card
import streamlit_authenticator as stauth
from db_api import create_connection
import yaml
from yaml.loader import SafeLoader

connection = create_connection()

st.set_page_config(page_title="Orders", page_icon="🛒")

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

sql = """\
    SELECT
        OrderHead.orderhead_id,
        OrderHead.orderhead_date,
        OrderDetail.product_id,
        Product.product_name,
        OrderDetail.quantity
        FROM OrderHead
        INNER JOIN OrderDetail ON OrderDetail.orderhead_id = OrderHead.orderhead_id
        INNER JOIN Product ON Product.product_id = OrderDetail.product_id
    WHERE
        OrderHead.user_id = ?
    ORDER BY OrderHead.orderhead_date DESC, OrderHead.orderhead_id DESC"""
rows = connection.new_cursor().execute(sql, (8,)).fetchall()
if len(rows) == 0:
    st.markdown('# No order yet...')
else:
    st.markdown('# Orders')
prior_order_id = 0
for row in rows:
    order_id = row[0]
    order_date = row[1]
    product_id = row[2]
    product_name = row[3]
    quantity = row[4]
    if order_id != prior_order_id:
        st.markdown(f"## Order n°{order_id} date : {order_date}")
    prior_order_id = order_id
    st.markdown(f"* Product n°{product_id} — {product_name} Qt : {quantity}")