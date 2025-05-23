import streamlit as st

def get_card_style():
    """
    Function to set the CSS styles for the product cards.
    This function is called in the main script to apply the styles.
    """
    # CSS for product card with wider image

    st.markdown(
    """<style>
        # .product-card-wide {
        #     background-color: #ffffff;
        #     border-radius: 12px;
        #     box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        #     padding: 16px;
        #     margin-bottom: 16px;
        #     width: 100%;
        #     text-align: center;
        #     font-family: 'Segoe UI', sans-serif;
        #     display: flex;
        #     flex-direction: column;
        #     align-items: center;
        # }

        # .product-card-content img {
        #     width: 100%;
        #     height: 180px;
        #     object-fit: cover;
        #     border-radius: 8px;
        #     margin-bottom: 16px;
        #     transition: transform 0.1s ease, box-shadow 0.2s ease;
        # }
        
        .product-card-wide {
            background-color: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
            padding: 16px;
            margin-bottom: 16px;
            width: 100%;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        
        .product-card-link {
            text-decoration: none !important;
            color: inherit;
            display: block;
        }
        
        .product-card-wide img {
            width: 100%;
            height: 180px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 16px;
            transition: transform 0.1s ease, box-shadow 0.2s ease;
        }

        .product-title {
            font-size: 18px;
            font-weight: 600;
            margin-bottom: 8px;
        }

        .product-price {
            font-size: 16px;
            color: #b12704;
            margin-bottom: 16px;
        }
        
        .product-button {
            # background-color: transparent;
            color: #111;
            padding: 8px 12px;
            border: 1px solid #ccc;
            border-radius: 4px;
            text-decoration: none !important;
            font-size: 14px;
            font-weight: 400;
            transition: all 0.2s ease;
            display: inline-block;
            cursor: pointer;
        }

        .product-button:hover {
            background-color: #f6f6f6;
            border-color: #999;
            text-decoration: none !important;
        }
        
        .product-description {
            margin-bottom: 16px;
        }

        div.stButton > button {
            width: 100%;
            border-radius: 6px;
            padding: 8px 0;
            font-size: 14px;
            margin-top: 4px;
            color: #111;
            border: 1px solid #ccc;
            cursor: pointer;
            transition: all 0.2s ease;
        }

        div.stButton > button:hover {
            background-color: #f6f6f6;
            border-color: #999;
        }
        </style>


    """,
        unsafe_allow_html=True,
    )
    
def get_background_style():
    """
    Function to set the CSS styles for the background.
    This function is called in the main script to apply the styles.
    """
    
    st.markdown(
    """<style>
        .stApp {
            background-image: url("https://bikes.com/cdn/shop/files/RM_MY25_NewColours_Growler_Opt2.jpg?v=1738878774&width=2880");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .stApp > header {       
            background-color: transparent;
        }
        </style>
    """,
        unsafe_allow_html=True,
    )