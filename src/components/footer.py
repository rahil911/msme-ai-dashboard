import streamlit as st
def render_footer():
    st.markdown("""
    <div class="cyber-footer"><div class="footer-content">
        <p>&copy; 2024 QUANTUM MSME ANALYTICS ⚡ All Rights Reserved</p>
        <p>Powered by Streamlit & OpenAI | Designed for Strategic Foresight</p>
        <div class="footer-links"><a href="#">Privacy Policy</a> | <a href="#">Terms of Service</a> | <a href="#">Contact Us</a></div>
    </div></div>
    """, unsafe_allow_html=True)
