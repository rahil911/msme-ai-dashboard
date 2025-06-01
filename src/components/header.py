import streamlit as st

def render_header():
    st.markdown("""
    <div class="main-header">
        <h1 style="font-size: 3.5rem; font-weight: 900; margin-bottom: 1rem; color: #00ffff; font-family: 'Orbitron', monospace; text-shadow: 0 0 20px rgba(0, 255, 255, 0.6);">
            ⚡ QUANTUM MSME ANALYTICS
        </h1>
        <p style="font-size: 1.4rem; color: #ff0080; margin-bottom: 0.5rem; font-family: 'Orbitron', monospace; letter-spacing: 2px;">
            NEURAL BUSINESS INTELLIGENCE MATRIX
        </p>
        <p style="font-size: 1.1rem; color: rgba(0, 255, 255, 0.8); font-family: 'Inter', sans-serif;">
            🧠 AI-POWERED ANALYTICS • 🚀 PREDICTIVE INTELLIGENCE • ⚡ REAL-TIME INSIGHTS
        </p>
        <div style="margin-top: 1rem; font-size: 0.9rem; color: rgba(255, 0, 128, 0.7);">
            🌐 Indian MSME Ecosystem • 📈 Data-Driven Decisions • 🔮 Future Forecasting
        </div>
    </div>
    """, unsafe_allow_html=True)
