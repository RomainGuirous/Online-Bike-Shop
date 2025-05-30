import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit_utils as st_utils
from style.style import get_card_style

st.set_page_config(page_title="modifier utilisateur")
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

if st.session_state.get("authentication_status"):
    try:
        if authenticator.update_user_details(st.session_state.get("username")):
            st.success("Entries updated successfully")
            with open("config.yaml", "w") as file:
                yaml.dump(config, file, default_flow_style=False, allow_unicode=True)
    except Exception as e:
        st.error(e)
