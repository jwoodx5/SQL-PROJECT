from project import create_table, get_connection, check_duplicate_customer, insert_data
# import pages.home as home
import streamlit as st
# from pages.home import cx_app
from pages import home, fire, water, mold



def app():
    st.title("Home page")
    options = [
        "--Make a Selection--",
        "Create Customer",
        "Water Readings",
        "Fire Readings",
        "Mold Readings"]

    selection = st.selectbox("Go To", options)

    if selection == "Create Customer":
        home.cx_app()
    elif selection == "Water Readings":
        water.app()
    elif selection == "Fire Readings":
        fire.app()
    elif selection == "Mold Readings":
        mold.app()




if __name__ == '__main__':
    app()
    # check_duplicate_customer(email) #debug <---
    create_table()
