import streamlit as st
from server import util

# Page config
st.set_page_config(page_title="Real Estate Price Predictor", layout="centered")

# Load backend
util.load_saved_artifacts()

st.markdown("""
    <style>
    body {
        background-color: #0b0f19;
    }

    .main {
        background: linear-gradient(135deg, #0b0f19, #111827);
        color: white;
    }

    h1 {
        color: #d4af37;
        text-align: center;
        font-size: 42px;
        margin-bottom: 10px;
    }

    .subtitle {
        text-align: center;
        color: #9ca3af;
        margin-bottom: 30px;
    }

    .input-box {
        background: #111827;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border: 1px solid #1f2937;
    }

    .stNumberInput input, .stSelectbox div {
        background-color: #1f2937 !important;
        color: white !important;
        border-radius: 8px !important;
    }

    .stButton>button {
        width: 100%;
        background: linear-gradient(90deg, #d4af37, #facc15);
        color: black;
        font-size: 20px;
        border-radius: 12px;
        padding: 12px;
        border: none;
        margin-top: 20px;
    }

    .result-box {
        background: linear-gradient(135deg, #111827, #1f2937);
        padding: 25px;
        border-radius: 20px;
        text-align: center;
        font-size: 28px;
        color: #00ffcc;
        margin-top: 30px;
        border: 1px solid #374151;
        box-shadow: 0px 0px 20px rgba(212, 175, 55, 0.2);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1>Real Estate Price Estimator</h1>", unsafe_allow_html=True)
st.markdown('<div class="subtitle">AI-powered Real Estate Valuation</div>', unsafe_allow_html=True)

sqft = st.number_input("📐 Total Square Feet", value=1000)

bhk = st.number_input("🛏️ Number of Bedrooms (BHK)", value=2)

bath = st.number_input("🛁 Number of Bathrooms", value=2)

location = st.selectbox("📍 Select Location", util.get_location_names())

# Button
if st.button("💰 Calculate Price"):
    price = util.get_estimated_price(location, sqft, bath, bhk)

    st.markdown(
        f"""
        <div class="result-box">
            💎 Estimated Property Value <br><br>
            ₹ {price} Lakhs
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("""
<hr style="
    border: none;
    height: 1px;
    background: linear-gradient(to right, transparent, #d4af37, transparent);
    margin: 30px 0;
">
""", unsafe_allow_html=True)

st.info("💡 Note: Property price depends more on location & area than number of rooms alone.")