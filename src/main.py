# main application logic, launch streamlit app, etc.
import streamlit as st
from database import create_connection, close_connection
from config import DB_FILE

def main():
    conn = create_connection(DB_FILE)
    if conn:
        # Run your application logic here
        close_connection(conn)
    else:
        st.error("Failed to connect to the database.")
        st.stop()
        
if __name__ == "__main__":
    main()