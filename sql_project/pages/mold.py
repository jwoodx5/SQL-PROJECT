import streamlit as st

def app():
    st.title("Mold Readings")

    # Collect mold readings using Streamlit components
    mold_date = st.date_input("Mold Date")
    mold_level = st.selectbox("Mold Level", ["Low", "Medium", "High"])
    mold_reading = st.number_input("Mold Reading")
    mold_location = st.text_input("Mold Location")

    # Create a button to submit the form
    if st.button("Submit Mold Readings"):
        if mold_date and mold_level and mold_location:
            # Implement code to save mold readings to the database here (if needed)
            st.success("Mold readings submitted successfully.")
            # Reset the input fields after successful submission
            st.date_input("Mold Date", value=None)
            st.selectbox("Mold Level", ["Low", "Medium", "High"], index=0)
            st.text_input("Mold Location", value="")
        else:
            st.warning("Please fill in all the fields.")