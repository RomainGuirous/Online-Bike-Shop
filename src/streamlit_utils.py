import yaml
from yaml.loader import SafeLoader
import streamlit
import streamlit_authenticator as stauth
from basket import Basket


def handle_access_rights(
    authorized_role: str, error_message: str = "Access denied."
) -> None:
    """
    Handle access rights for the Streamlit application.
    This function checks if the user has the required role to access the application.
    If the user does not have the required role, it displays an error message
    and provides an option to log in.

    Args:
        authorized_role (str): The role required to access the application.
        error_message (str): The message to display if access is denied.

    Returns:
        stauth.Authenticate: An instance of the Authenticate class for user authentication.
    """

    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        api_key=config["api_key"],
    )

    if authorized_role not in (streamlit.session_state.get("roles") or []):
        streamlit.error(error_message)
        if streamlit.button("Login"):
            streamlit.switch_page("pages/connection.py")
        streamlit.stop()
    if streamlit.session_state.get("authentication_status"):
        streamlit.success(f"Welcome {streamlit.session_state['name']}!")
        authenticator.logout()
        if streamlit.button("Modify user details"):
            streamlit.switch_page("pages/update_user.py")
    return authenticator


def show_global_menu() -> None:
    """
    Display a global menu in the Streamlit app.
    This function creates a horizontal navigation menu with links to different pages
    of the application, allowing users to navigate between the home, catalogue, basket,
    orders, and admin pages.
    """

    col_1, col_2, col_3, col_4, col_5 = streamlit.columns(5)
    with col_1:
        if streamlit.button("Home"):
            streamlit.switch_page("main.py")
    with col_2:
        if streamlit.button("Catalogue"):
            streamlit.switch_page("pages/catalogue.py")
    with col_3:
        if streamlit.button("Basket"):
            streamlit.switch_page("pages/basket.py")
    with col_4:
        if streamlit.button("Orders"):
            streamlit.switch_page("pages/orders.py")
    with col_5:
        if streamlit.button("Admin"):
            streamlit.switch_page("pages/admin.py")


def get_session_basket() -> Basket:
    """
    Retrieve the shopping basket from the session state.
    If the basket does not exist, it initializes a new Basket instance.

    Returns:
        Basket: The shopping basket instance from the session state.
    """
    if "basket" not in streamlit.session_state:
        streamlit.session_state["basket"] = Basket()
    return streamlit.session_state["basket"]


def event_add_to_basket(product_id: int) -> None:
    """
    Handle the event of adding a product to the basket.
    This function updates the session state with the product ID to be added
    and switches to the basket page.

    Args:
        product_id (int): The ID of the product to add to the basket.
    """
    streamlit.session_state["product_to_add_to_basket"] = product_id
    streamlit.switch_page("pages/basket.py")


def hide_sidebar_pages() -> None:
    """
    Hide the sidebar in Streamlit.
    This function injects custom CSS to hide the sidebar and the collapsed control.
    """
    return streamlit.markdown(
        """
    <style>
        [data-testid="stSidebar"] {
            display: none;
        }
        [data-testid="collapsedControl"] {
            display: none;
        }
    </style>
    """,
        unsafe_allow_html=True,
    )
