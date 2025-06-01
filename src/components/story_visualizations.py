import streamlit as st
import os
def render_story_visualizations():
    st.markdown('<h2 class="section-header">🖼️ UNIFIED STORY VISUALIZATIONS</h2>', unsafe_allow_html=True)
    viz_tabs = st.tabs(["📊 Ch1: Eco Foundation", "🎯 Ch2: MSME Oppy", "🌐 Ch3: Export Pathway"])
    img_paths = ['output/images/chapter1_economic_foundation.png', 'output/images/chapter2_msme_opportunities.png', 'output/images/chapter3_export_pathway.png']
    captions = ["Ch1: Eco Foundation", "Ch2: MSME Opportunities", "Ch3: Export Pathway"]
    for i, tab in enumerate(viz_tabs):
        with tab:
            st.markdown(f"### {captions[i]}")
            if os.path.exists(img_paths[i]): st.image(img_paths[i], caption=captions[i], use_column_width=True)
            else: st.error(f"Image not found: {img_paths[i]}")
    st.info("💡 Actual visualizations from unified MSME story analysis.")
