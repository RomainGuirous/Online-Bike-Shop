# main application logic, launch streamlit app, etc.
import streamlit as st
from products.utils import get_best_selling_products
from db_api import DBConnection
from config import DB_FILE
from style.style import get_card_style, get_background_style

st.set_page_config(
    page_title="Page d'accueil",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="🚴",
)


def get_product_card(product):
    return f"""
    <div class="product-card-wide">
        <img src="{product["picture"]}" alt="Bike Image">
        <div class="product-title">{product["product_name"]}</div>
        <div class="product-price">{product["price"]}</div>
    </div>
    """
    
def main():

    get_background_style()

    # initialize session state
    if "connection" not in st.session_state:
        st.session_state["connection"] = None

    if "role" not in st.session_state:
        st.session_state["role"] = "default"  # Default role

    conn = DBConnection(DB_FILE)
    st.session_state["connection"] = conn

    if conn:
        products = get_best_selling_products(conn)
        
    else:
        st.error("Database connection failed.")
        st.stop()

    # Inject global styles
    get_card_style()
        
    st.image(
        "https://images.squarespace-cdn.com/content/v1/5d9a1d9c10aea63ab743558c/62ba744d-87f8-44ee-8a80-9d0988aa19c5/2025_The-Big-Velo-Bike-Sale-Home-Page-Images-9-website+homepage+image.png",
        use_container_width=True,
        width=700
    )

    st.markdown(
        """
        <h2 style="text-align: center; color: #FFFFFF;">Best selling products</h2>
        """,
        unsafe_allow_html=True,
    )
    
    # Display cards in a 4-column responsive layout
    cols_per_row = 4
    for i in range(0, len(products), cols_per_row):
        row = st.columns(cols_per_row)
        for j in range(cols_per_row):
            if i + j < len(products):
                product = products[i + j]
                with row[j]:

                    # Card HTML
                    st.markdown(get_product_card(product), unsafe_allow_html=True)
    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("🛒 Add to Cart", key=f"cart_{product['product_id']}"):
                            st.session_state.id = product['product_id']
                            st.switch_page("pages/basket.py")
                    with col2:
                        if st.button("🔍 View Details", key=f"details_{product['product_id']}"):
                            st.session_state.id = product['product_id']
                            st.switch_page("pages/product.py")

    
if __name__ == "__main__":
    main()
