import streamlit
from basket import Basket

def get_session_basket()-> Basket:
    if 'basket' not in streamlit.session_state:
        streamlit.session_state["basket"] = Basket()
    return streamlit.session_state["basket"]

def event_add_to_basket(product_id: int)-> None:
    streamlit.session_state["product_to_add_to_basket"] = product_id
    streamlit.switch_page("pages/basket.py")