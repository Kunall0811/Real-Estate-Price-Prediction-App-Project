import streamlit as st
from server import util

# Load model + data
util.load_saved_artifacts()

# 🎯 PAGE CONFIG
st.set_page_config(
    page_title="Real Estate Price Predictor",
    page_icon="🏡",
    layout="centered"
)

# 🎨 HEADER
st.markdown("""
    <h1 style='text-align: center; color: #2E86C1;'>
        🏡 Real Estate Price Estimator
    </h1>
    <p style='text-align: center; color: gray;'>
        AI-powered real estate valuation system
    </p>
""", unsafe_allow_html=True)

st.markdown("---")

# 📥 INPUT SECTION 
sqft = st.number_input("📏 Total Square Feet", value=1000)

bhk = st.number_input("🛏️ BHK (Bedrooms)", value=2)

bath = st.number_input("🚿 Bathrooms", value=2)

location = st.selectbox("📍 Location", util.get_location_names())

st.markdown("---")

# 🚀 PREDICTION
if st.button("💰 Predict Price"):

    # Feature engineering insight
    avg_room_size = sqft / bhk

    # Prediction
    price = util.get_estimated_price(location, sqft, bath, bhk)

    # 💎 RESULT CARD
    st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #1f1c2c, #928DAB);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
            font-size: 32px;
            font-weight: bold;
            box-shadow: 0px 4px 20px rgba(0,0,0,0.3);
        ">
            ₹ {price} Lakhs
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # 📊 INSIGHTS CARD
    st.markdown(f"""
        <div style="
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
        ">
            <h4>📊 Property Insights</h4>
            <p>📍 Location: {location}</p>
            <p>📏 Total Area: {sqft} sq ft</p>
            <p>🛏️ BHK: {bhk}</p>
            <p>🚿 Bathrooms: {bath}</p>
            <p>📐 Avg Room Size: {round(avg_room_size, 2)} sq ft</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

st.info("💡 Note: Property price depends more on location & area than number of rooms alone.")