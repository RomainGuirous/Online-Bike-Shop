import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit_utils as st_utils
from style.style import get_card_style

st.set_page_config(page_title="Register", page_icon="📝", layout="centered")
get_card_style()
st_utils.hide_sidebar_pages()
st_utils.show_global_menu()

with open("config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config["credentials"],
    config["cookie"]["name"],
    config["cookie"]["key"],
    config["cookie"]["expiry_days"],
    api_key=config["api_key"],
)

try:
    email_of_registered_user, username_of_registered_user, name_of_registered_user = (
        authenticator.register_user(roles=["user", "admin"])
    )
    if email_of_registered_user:
        st.success("User registered successfully")
        with open("config.yaml", "w") as file:
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True)
        st.switch_page("pages/connection.py")
except Exception as e:
    st.error(e)
