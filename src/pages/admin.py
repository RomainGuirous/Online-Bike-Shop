import streamlit as st
from orders.utils import get_order_list
from products.utils import get_product_dataframe
from users.utils import get_user_list
from db_api import create_connection
import plotly.express as px
import streamlit_utils as st_utils



st.set_page_config(page_title="Admin Dashboard", page_icon="🛠️", layout="wide")

# --- AUTH ---
conn = create_connection()
st_utils.handle_access_rights('admin')

tabs = st.tabs(["📦 Orders", "🛍️ Products", "👤 Users"])

order_df = get_order_list(conn)
product_df = get_product_dataframe(conn)
user_df = get_user_list(conn)

# add product price in order_df
if order_df is not None and not order_df.empty:
    order_df = order_df.merge(product_df[["product_id", "price"]], on="product_id", how="left")
    order_df["total"] = order_df["quantity"] * order_df["price"]


# --- ORDERS ---
with tabs[0]:
    order_df["total"] = order_df["quantity"] * order_df["price"]
    order_df["total"] = order_df["total"].str.replace("€", "").str.replace(",", ".").astype(float)
    st.subheader("📦 Order Data")

    if order_df is not None and not order_df.empty:
        with st.expander("🔍 View Full Table"):
            
            st.dataframe(order_df)

        # Summary
        st.markdown("#### 📊 Order Stats")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Orders", len(order_df.groupby("orderhead_id")))
        with col2:
            st.metric("Total Revenue", f"${order_df['total'].sum():,.2f}")

        # Time-based sales chart
        if "orderhead_date" in order_df.columns:
            df_by_day = order_df.groupby("orderhead_date")["total"].sum().reset_index()
            fig = px.line(df_by_day, x="orderhead_date", y="total", title="Revenue Over Time")
            st.plotly_chart(fig, use_container_width=True)

# --- PRODUCTS ---
with tabs[1]:
    st.subheader("🛍️ Product Data")

    if product_df is not None and not product_df.empty:
        with st.expander("🔍 View Full Table"):
            st.dataframe(product_df)

        # Top-selling products (if available)
        if "sales" in product_df.columns:
            top_products = product_df.sort_values(by="sales", ascending=False).head(10)
            fig = px.bar(top_products, x="product_name", y="sales", title="Top Selling Products")
            st.plotly_chart(fig, use_container_width=True)

# --- USERS ---
with tabs[2]:
    st.subheader("👤 User Data")

    if user_df is not None and not user_df.empty:
        with st.expander("🔍 View Full Table"):
            st.dataframe(user_df)

        st.markdown("#### 👥 User Summary")
        st.metric("Total Users", len(user_df))

        # User roles pie chart (if roles exist)
        if "role" in user_df.columns:
            role_counts = user_df["role"].value_counts().reset_index()
            role_counts.columns = ["Role", "Count"]
            fig = px.pie(role_counts, names="Role", values="Count", title="User Roles")
            st.plotly_chart(fig, use_container_width=True)
