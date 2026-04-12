import streamlit as st
import util

# Load model + columns
util.load_saved_artifacts()

st.set_page_config(page_title="Real Estate Price Estimation", layout="centered")

st.title("🏠 Real Estate Price Prediction App")
st.markdown("Enter property details below to estimate price")

# Get data
locations = util.get_location_names()

# Inputs
location = st.selectbox("📍 Location", locations)

total_sqft = st.number_input("📐 Total Square Feet", min_value=300.0, step=50.0)

bhk = st.number_input("🛏️ BHK", min_value=1, step=1)

bath = st.number_input("🚿 Bathrooms", min_value=1, step=1)

# Predict button
if st.button("Predict Price"):

    prediction = util.get_estimated_price(
        location,
        total_sqft,
        bhk,
        bath
    )

    st.success(f"Estimated Price: ₹ {round(prediction, 2)} Lakhs")

# Footer note
st.markdown("---")

st.info("💡 Note: Property price depends more on location, room space efficiency than number of rooms alone.")