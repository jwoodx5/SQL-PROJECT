import streamlit as st

def app():
    st.title("Fire Readings")

    # Collect fire readings using Streamlit components
    fire_date = st.date_input("Fire Date")
    damage_extent = st.selectbox("Damage Extent", ["Low", "Medium", "High"])
    damage_extent = st.text_input("Damage Information")
    cause = st.text_input("Cause of Fire")

    # Create a button to submit the form
    if st.button("Submit Fire Readings"):
        if fire_date and damage_extent and cause:
            # Implement code to save fire readings to the database here (if needed)
            st.success("Fire readings submitted successfully.")
            # Reset the input fields after successful submission
            st.date_input("Fire Date", value=None)
            st.selectbox("Damage Extent", ["Low", "Medium", "High"], index=0)
            st.text_input("Cause of Fire", value="")
        else:
            st.warning("Please fill in all the fields.")