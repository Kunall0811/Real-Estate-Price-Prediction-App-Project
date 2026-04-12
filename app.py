import streamlit as st
from server import util

# Load model + columns
util.load_saved_artifacts()

# Page config
st.set_page_config(
    page_title="Real Estate Price Estimation",
    layout="centered"
)

# UI Header
st.markdown(
    "<h1 style='text-align:center;'>Real Estate Price Prediction App</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<h4 style='text-align:center; color:gray;'>Enter property details below to estimate price</h4>",
    unsafe_allow_html=True
)

# Load locations
locations = util.get_location_names()

# Inputs
location = st.selectbox("📍 Location", locations)

total_sqft = st.number_input(
    "📐 Total Square Feet",
    min_value=300.0,
    step=50.0
)

bhk = st.number_input(
    "🛏️ BHK",
    min_value=1,
    step=1
)

bath = st.number_input(
    "🚿 Bathrooms",
    min_value=1,
    step=1
)

# Predict button
if st.button("Predict Price"):

    prediction = util.get_estimated_price(
        location,
        total_sqft,
        bhk,
        bath
    )

    st.success(f"Estimated Price: ₹ {round(prediction, 2)} Lakhs")


st.markdown("---")

# Footer note
st.markdown(
    """
    <div style="
        text-align:center;
        padding:12px;
        background: linear-gradient(90deg, #fffef5, #fffcea);
        border-radius:10px;
        color:#7a5c00;
        font-weight:600;
        box-shadow: 0px 0px 10px rgba(255, 215, 0, 0.6);
        text-shadow: 0px 0px 6px rgba(255, 215, 0, 0.9);
    ">
    💡 Note: Property price depends more on location, area, and room space efficiency than just the number of rooms.
    </div>
    """,
    unsafe_allow_html=True
)