import streamlit as st
from streamlit_card import card
    
st.set_page_config(page_title="Catalogue",
                    page_icon="📚",
                   )

    
cols = st.columns(2)

for i in range(10):
    with cols[i % 2]:
        card(
            title="Bike" + str(i),
            text="This is a bike description.",
            image="https://via.placeholder.com/150",
            on_click=lambda: st.switch_page("pages/connection.py"),
            # styles={
            #     "card": {
            #         "width": "100%",
            #         "height": "100%",
            #         "border-radius": "10px",
            #         "box-shadow": "0 4px 8px rgba(0, 0, 0, 0.2)",
            #     },
            #     "title": {"font-size": "20px", "font-weight": "bold"},
            #     "text": {"font-size": "14px"},
            # },
        )
