import streamlit as st
from db_api import create_connection
import streamlit_utils as st_utils
from style.style import get_card_style
st.set_page_config(page_title="Orders", page_icon="🛒")
get_card_style()
st_utils.hide_sidebar_pages()
st_utils.show_global_menu()

st_utils.handle_access_rights("user", "Please sign in to access your orders.")

connection = create_connection()
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
    st.markdown("# No order yet...")
else:
    st.markdown("# Orders")
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
