import streamlit as st

def render_control_bar():
    ai_status = "🟢 NEURAL AI ONLINE"
    if 'openai_api_key' in st.session_state and st.session_state.openai_api_key:
        pass
    else:
        try:
            if "OPENAI_API_KEY" in st.secrets and st.secrets["OPENAI_API_KEY"]:
                 st.session_state.openai_api_key = st.secrets["OPENAI_API_KEY"]
            else:
                st.session_state.openai_api_key = ""
                ai_status = "🔴 AI OFFLINE"
        except Exception:
            st.session_state.openai_api_key = ""
            ai_status = "🔴 AI OFFLINE (Secrets error)"

    with st.container():
        st.markdown('<div class="top-control-bar">', unsafe_allow_html=True)
        control_cols = st.columns([2, 2, 2, 2, 1])
        if 'filters' not in st.session_state: st.session_state.filters = {}

        with control_cols[0]:
            st.markdown('<div class="control-group"><span class="control-label">⏱️ TIME RANGE</span></div>', unsafe_allow_html=True)
            year_range = st.slider("Years", min_value=2010, max_value=2030, value=st.session_state.filters.get('year_range', (2010, 2024)), label_visibility="collapsed")
            st.session_state.filters['year_range'] = year_range

        with control_cols[1]:
            st.markdown('<div class="control-group"><span class="control-label">🎯 ANALYSIS MODE</span></div>', unsafe_allow_html=True)
            analysis_options = ["Complete Analysis", "Economic Foundation", "Sector Opportunities", "Export Strategy", "Regional Analysis"]
            current_analysis_type = st.session_state.filters.get('analysis_type', analysis_options[0])
            try: current_analysis_index = analysis_options.index(current_analysis_type)
            except ValueError: current_analysis_index = 0
            analysis_type = st.selectbox("Analysis", analysis_options, index=current_analysis_index, label_visibility="collapsed")
            st.session_state.filters['analysis_type'] = analysis_type

        with control_cols[2]:
            st.markdown('<div class="control-group"><span class="control-label">🏭 SECTOR FOCUS</span></div>', unsafe_allow_html=True)
            available_sectors = ['Digital Commerce', 'Financial Services', 'Healthcare Tech', 'Agriculture Tech', 'Manufacturing', 'Education Tech', 'Renewable Energy', 'Food Processing']
            selected_sectors = st.multiselect("Sectors", available_sectors, default=st.session_state.filters.get('sectors', []), label_visibility="collapsed")
            st.session_state.filters['sectors'] = selected_sectors

        with control_cols[3]:
            st.markdown('<div class="control-group"><span class="control-label">🔮 PROJECTION</span></div>', unsafe_allow_html=True)
            time_horizon_options = ["Current (2024)", "Short-term (2025-2027)", "Long-term (2027-2030)"]
            current_time_horizon = st.session_state.filters.get('time_horizon', time_horizon_options[0])
            try: current_horizon_index = time_horizon_options.index(current_time_horizon)
            except ValueError: current_horizon_index = 0
            time_horizon = st.selectbox("Horizon", time_horizon_options, index=current_horizon_index, label_visibility="collapsed")
            st.session_state.filters['time_horizon'] = time_horizon

        with control_cols[4]:
            st.markdown(f'<div class="control-group"><span class="control-label">🤖 AI STATUS</span><br/><span style="color: #00ffff; font-weight: bold; font-size: 0.8rem;">{ai_status}</span></div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
