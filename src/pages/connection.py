import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit_utils as st_utils
from style.style import get_card_style

st.set_page_config(page_title="Connection", page_icon="🔑", layout="centered")
get_card_style()
st_utils.hide_sidebar_pages()
st_utils.show_global_menu()

with st.spinner("Please wait..."):
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    # Pre-hashing all plain text passwords once
    stauth.Hasher.hash_passwords(config["credentials"])

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
    )

    try:
        authenticator.login()
    except Exception as e:
        st.error(e)

    try:
        authenticator.experimental_guest_login(
            "Login with Google", provider="google", oauth2=config["oauth2"]
        )
        authenticator.experimental_guest_login(
            "Login with Microsoft", provider="microsoft", oauth2=config["oauth2"]
        )
    except Exception as e:
        st.error(e)

    if st.session_state.get("authentication_status"):
        st.success(f"Welcome {st.session_state['name']}!")
        authenticator.logout()
        if "admin" in st.session_state.get("roles", []):
            st.switch_page("pages/admin.py")
        else:
            st.switch_page("pages/basket.py")
        st.write(st.session_state)
    elif st.session_state.get("authentication_status") is False:
        st.error("Username/password is incorrect")
    elif st.session_state.get("authentication_status") is None:
        st.warning("Please enter your username and password")
