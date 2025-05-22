import streamlit as st
import streamlit_authenticator as stauth
from yaml import SafeLoader
import yaml

st.set_page_config(page_title="Admin", page_icon="🛠️")


with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

if "admin" not in (st.session_state.get("roles") or []):
    st.error("Access denied. You are not an admin.")
    if st.button("Login"):
        st.switch_page("pages/connection.py")

    
if st.session_state.get('authentication_status'):
    st.success(f'Welcome {st.session_state["name"]}!')
    authenticator.logout()
