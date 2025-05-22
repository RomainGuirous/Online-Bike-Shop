import streamlit as st
from streamlit_card import card
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(page_title="Catalogue", page_icon="🛒")

with open('config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

if "user" not in (st.session_state.get("roles") or []):
    st.error("you must be logged in to access this page.")
    
    if st.button("Login"):
        st.switch_page("pages/connection.py")
    st.stop()
    
if st.session_state.get('authentication_status'):
    st.success(f'Welcome {st.session_state["name"]}!')
    authenticator.logout()


cols = st.columns(2)

for i in range(10):
    with cols[i % 2]:
        card(
            title="Bike" + str(i),
            text="This is a bike description.",
            image="https://via.placeholder.com/150",
            on_click=lambda: st.switch_page("pages/connection.py"),
        )
