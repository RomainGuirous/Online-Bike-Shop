import streamlit as st
import streamlit_authenticator as stauth
from yaml import SafeLoader
import yaml
import streamlit_utils as st_utils

st.set_page_config(page_title="Admin", page_icon="🛠️")

st_utils.handle_access_rights('admin')
