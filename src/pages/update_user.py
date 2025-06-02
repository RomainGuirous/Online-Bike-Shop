import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader
import streamlit_utils as st_utils
from style.style import get_card_style
from users.models import User
from db_api import create_connection
from users.utils import get_user_id_from_username


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
    if authenticator.update_user_details(st.session_state.get("username")):
        with open("config.yaml", "w") as file:
            yaml.dump(config, file, default_flow_style=False, allow_unicode=True)
        conn = create_connection()
        user_id = get_user_id_from_username(conn, st.session_state.get("username"))

        user = config["credentials"]["usernames"][st.session_state.get("username")]
        user_model = User(db_connection=conn, is_new=False, user_id=user_id)
        user_model.first_name = user["first_name"]
        user_model.last_name = user["last_name"]
        user_model.email = user["email"]
        user_model.save_to_db()
        conn.commit()
        st.success("Entries updated successfully")
