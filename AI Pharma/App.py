import streamlit as st

# Set up the main app configuration
st.set_page_config(page_title="AI Pharma", page_icon="💊", layout="wide")

# Logo and Name (Top-Left)
col1, col2 = st.columns([0.15, 0.85])  # Adjust column width as needed
with col1:
    st.image("assets/logo.png", width=80)  # Circular effect applied below
with col2:
    st.markdown("<h1 style='color: #4CAF50;'>AI Pharma</h1>", unsafe_allow_html=True)

# Add a horizontal line to separate logo from welcome text
st.markdown("<hr style='border: 1px solid #ddd; margin: 20px 0;'>", unsafe_allow_html=True)

# Centered Welcome Message
st.markdown(
    """
    <div style="text-align: center;">
        <h1 style="color: #4CAF50;">Welcome to AI-Pharma</h1>
        <p style="font-size: 20px; font-style: italic; color: #555;">Empowering Healthcare with Intelligent Insights</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Custom CSS for Circular Logo
st.markdown(
    """
    <style>
        img {
            border-radius: 50%;  /* Circular shape */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Feature Highlights
st.markdown("### 🔥 Features")
col1, col2, col3 = st.columns(3)
with col1:
    st.info("📷 **Upload & Analyze** - Upload prescriptions and extract text.")
with col2:
    st.success("💊 **AI Suggestions** - Get AI-based medicine recommendations.")
with col3:
    st.warning("📈 **Insights** - Track and analyze prescription data.")

st.markdown("---")
st.write("🔹 Use the sidebar to navigate!")
