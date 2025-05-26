import yaml
from yaml.loader import SafeLoader
import streamlit
import streamlit_authenticator as stauth
from basket import Basket


def handle_access_rights(
    authorized_role: str, error_message: str = "Access denied."
) -> None:
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)
    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )
    if authorized_role not in (streamlit.session_state.get("roles") or []):
        streamlit.error(error_message)
        if streamlit.button("Login"):
            streamlit.switch_page("pages/connection.py")
        streamlit.stop()
    if streamlit.session_state.get("authentication_status"):
        streamlit.success(f"Welcome {streamlit.session_state['name']}!")
        authenticator.logout()
    return authenticator


def show_global_menu() -> None:
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
    if "basket" not in streamlit.session_state:
        streamlit.session_state["basket"] = Basket()
    return streamlit.session_state["basket"]


def event_add_to_basket(product_id: int) -> None:
    streamlit.session_state["product_to_add_to_basket"] = product_id
    streamlit.switch_page("pages/basket.py")


def hide_sidebar_pages():
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
