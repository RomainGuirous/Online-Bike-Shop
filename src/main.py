# main application logic, launch streamlit app, etc.
import streamlit as st
from products.utils import get_best_selling_products
from db_api import create_connection, ConnectionType
from style.style import get_card_style, get_background_style
import streamlit_utils as st_utils


def get_product_card(product) -> str:
    """
    Generate HTML for a product card.

    Args:
        product (dict): A dictionary containing product details.

    Returns:
        str: HTML string for the product card.
    """
    return f"""
    <div class="product-card-wide">
        <img src="{product["picture"]}" alt="Bike Image">
        <div class="product-title">{product["product_name"].capitalize()}</div>
        <div class="product-price">{product["price"]} ¥</div>
    </div>
    """


def main():
    """
    Main function to run the Streamlit application.
    This function sets up the page configuration, connects to the database,
    retrieves the best-selling products, and displays them in a responsive layout
    with interactive buttons for adding to cart and viewing details.
    It also includes global styles and a background image for the app.
    The products are displayed in a grid format with cards that include product images,
    names, and prices. Each product card has buttons for adding the product to the cart
    and viewing more details, which switch to the product detail page when clicked.
    The page is designed to be responsive and visually appealing, with a focus on user experience.
    It also handles session state to maintain user interactions across different pages.

    :return: None
    """

    st.set_page_config(
        page_title="Page d'accueil",
        layout="wide",
        initial_sidebar_state="expanded",
        page_icon="🚴",
    )

    st_utils.hide_sidebar_pages()
    st_utils.show_global_menu()
    get_background_style()

    if "role" not in st.session_state:
        st.session_state["role"] = "default"  # Default role

    conn = create_connection()

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
        width=700,
    )

    st.markdown(
        """
        <h2 style="text-align: center; color: #FFFFFF;">Best selling products</h2>
        """,
        unsafe_allow_html=True,
    )

    if conn.is_of_type(ConnectionType.MONGODB):
        product_id_name = '_id'
    else:
        product_id_name = 'product_id'

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
                        if st.button(
                            "🛒 Add to Cart", key=f"cart_{product[product_id_name]}"
                        ):
                            st.session_state.id = product[product_id_name]
                            st_utils.event_add_to_basket(product[product_id_name])

                    with col2:
                        if st.button(
                            "🔍 View Details", key=f"details_{product[product_id_name]}"
                        ):
                            st.session_state.id = product[product_id_name]
                            st.switch_page("pages/product.py")


if __name__ == "__main__":
    main()
