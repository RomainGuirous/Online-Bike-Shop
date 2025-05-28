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
        api_key=config["api_key"],
    )

    try:
        authenticator.login(captcha=True)
    except Exception as e:
        st.error(e)
    if st.button("Register"):
        st.switch_page("pages/register.py")

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

    try:
        username_of_forgotten_username, email_of_forgotten_username = (
            authenticator.forgot_username(two_factor_auth=True, send_email=True)
        )
        if username_of_forgotten_username:
            st.success("Username to be sent securely")
            # To securely transfer the username to the user please see step 8.
        elif username_of_forgotten_username == False:
            st.error("Email not found")
    except Exception as e:
        st.error(e)

    try:
        (
            username_of_forgotten_password,
            email_of_forgotten_password,
            new_random_password,
        ) = authenticator.forgot_password(two_factor_auth=True, send_email=True)
        if username_of_forgotten_password:
            st.success("New password to be sent securely")
            # To securely transfer the new password to the user please see step 8.
        elif username_of_forgotten_password == False:
            st.error("Username not found")
    except Exception as e:
        st.error(e)
