import streamlit as st
def render_metrics():
    st.markdown('<h2 class="section-header">📊 QUANTUM PERFORMANCE MATRIX</h2>', unsafe_allow_html=True)
    metric_cols = st.columns(4)
    with metric_cols[0]: st.markdown('<div class="metric-card"><div class="metric-label">📈 GDP GROWTH 2023</div><div class="metric-value">8.15%</div><div class="metric-description">EXACT World Bank data: 8.1529%</div><div style="color: #ff0080; font-weight: 600; margin-top: 0.5rem;">✅ WB Verified</div></div>', unsafe_allow_html=True)
    with metric_cols[1]: st.markdown('<div class="metric-card"><div class="metric-label">👥 LABOR FORCE 2024</div><div class="metric-value">607.7M</div><div class="metric-description">EXACT WB: 607,691,498 workers</div><div style="color: #ff0080; font-weight: 600; margin-top: 0.5rem;">✅ WB Official</div></div>', unsafe_allow_html=True)
    with metric_cols[2]: st.markdown('<div class="metric-card"><div class="metric-label">🌐 EXPORTS 2023</div><div class="metric-value">21.85%</div><div class="metric-description">EXACT WB: 21.8482% of GDP</div><div style="color: #ff0080; font-weight: 600; margin-top: 0.5rem;">✅ WB Data</div></div>', unsafe_allow_html=True)
    with metric_cols[3]: st.markdown('<div class="metric-card"><div class="metric-label">🚀 UNEMPLOYMENT 2024</div><div class="metric-value">4.20%</div><div class="metric-description">EXACT WB: 4.202% ILO estimate</div><div style="color: #ff0080; font-weight: 600; margin-top: 0.5rem;">✅ WB Verified</div></div>', unsafe_allow_html=True)
