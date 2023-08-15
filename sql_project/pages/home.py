import streamlit as st
from project import insert_data

def cx_app():
    st.title("Create a Customer")
    st.write("Add the customers First Name, Last Name, Email, Phone number, and address here:")
    customer_fname = st.text_input('Customer First Name:')
    customer_lname = st.text_input('Customer Last Name:')
    customer_email = st.text_input('Customer Email:')
    customer_phonenum = st.text_input('Customer Phone Number:')
    customer_address = st.text_input('Customer Address:')

    
    if st.button('Create Customer'):
        result = insert_data(customer_fname, customer_lname, customer_email, customer_phonenum, customer_address)
        if result:
            st.success('Customer Created Successfully')
        else:
            st.write('Error Creating the customer')

if __name__ == "__main__":
    cx_app()