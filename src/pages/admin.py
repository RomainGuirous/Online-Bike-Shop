import streamlit as st
from streamlit import session_state as st_session

if "role" not in st_session:
    st_session["role"] = "default"  # Default role

if st_session.get("role") != "admin":
    st.error("You need to be an admin to access this page.")
    st.stop()
