import streamlit as st
from db_api import create_connection, ConnectionType
from users.utils import get_user_id_from_username
import streamlit_utils as st_utils
from style.style import get_card_style

st.set_page_config(page_title="Orders", page_icon="🛒")
get_card_style()
st_utils.hide_sidebar_pages()
st_utils.show_global_menu()

st_utils.handle_access_rights("user", "Please sign in to access your orders.")
connection = create_connection()
user_id = get_user_id_from_username(connection, st.session_state["username"])
if connection.is_of_type(ConnectionType.SQLITE):
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
    rows = connection.new_query().execute(sql, (user_id,)).fetchall()
else:
    order_list = connection.new_query()['OrderHead'].find({'user_id': user_id}).sort("orderhead_date", -1)
    rows = []
    for order in order_list:
        for detail in order['OrderDetails']:
            row = {}
            row['orderhead_id'] = order['_id']
            row['orderhead_date'] = order['orderhead_date']
            row['product_id'] = detail['product_id']
            product_row = list(connection.new_query()['Product'].find({'_id': detail['product_id']}))[0]
            if product_row:
                row['product_name'] = product_row['product_name']
            else:
                row['product_name'] = '???'
            row['quantity'] = detail['quantity']
            rows.append(row)
if len(rows) == 0:
    st.markdown("# No order yet...")
else:
    st.markdown("# Orders")
prior_order_id = 0
for row in rows:
    if row['orderhead_id'] != prior_order_id:
        st.markdown(f"## Order n°{row['orderhead_id']} date : {row['orderhead_date']}")
    prior_order_id = row['orderhead_id']
    st.markdown(f"* Product n°{row['product_id']} — {row['product_name']} Qt : {row['quantity']}")