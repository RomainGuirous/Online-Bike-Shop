import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit_utils as st_utils
from style.style import get_card_style
from users.models import User
from db_api import create_connection

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
        conn = create_connection()
        user = config["credentials"]["usernames"][username_of_registered_user]
        new_user = User(db_connection=conn, is_new=True)
        new_user.first_name = user["first_name"]
        new_user.last_name = user["last_name"]
        new_user.email = email_of_registered_user
        new_user.username = username_of_registered_user
        new_user.hashed_password = user["password"]
        new_user.password_hint = user["password_hint"]
        user["roles"] = "admin" if "admin" in user["roles"] else "user"
        new_user.roles = user["roles"]

        new_user.save_to_db()
        conn.commit()
        # st.switch_page("pages/connection.py")


except Exception as e:
    st.error(e)
