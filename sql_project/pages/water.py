import streamlit as st

def app():
    st.title("Water Readings")

    # Collect water readings using Streamlit components
    water_date = st.date_input("Water Date")
    water_level = st.selectbox("Water Level", ["Low", "Medium", "High"])
    water_reading = st.number_input("Water Reading")
    water_source = st.text_input("Water Source")

    # Create a button to submit the form
    if st.button("Submit Water Readings"):
        if water_date and water_level and water_source:
            # Implement code to save water readings to the database here (if needed)
            st.success("Water readings submitted successfully.")
            # Reset the input fields after successful submission
            st.date_input("Water Date", value=None)
            st.selectbox("Water Level", ["Low", "Medium", "High"], index=0)
            st.text_input("Water Source", value="")
        else:
            st.warning("Please fill in all the fields.")