import streamlit as st
from src.utils.ai_helper import get_enhanced_chart_context, chat_with_ai_enhanced
from datetime import datetime

def render_ai_chat_panel(slides_data=None): # slides_data is optional
    if slides_data is None: slides_data = [] # Default to empty list
    with st.container():
        # Using a raw Python string for the HTML block to avoid issues with quotes and special characters
        # Ensure no leading spaces on the r''' line
        ai_panel_header_html = r'''
        <div class="ai-panel-container">
            <div class="ai-panel-header">
                <h3><span class="ai-icon">&#x1F916;</span> QUANTUM AI ANALYST</h3>
                <p>Your copilot for deep economic insights & strategic foresight.</p>
            </div>
        </div>
        '''
        st.markdown(ai_panel_header_html, unsafe_allow_html=True)

        openai_api_key_input = st.text_input(
            "🔑 Enter OpenAI API Key:", type="password",
            key="openai_api_key_input_chat_panel_v3",
            help="Required for AI analysis.",
            value=st.session_state.get("openai_api_key", "")
        )
        if openai_api_key_input: st.session_state.openai_api_key = openai_api_key_input

        if not st.session_state.get("openai_api_key"): st.warning("Please enter OpenAI API key.")
        else: st.success("OpenAI API Key active.")

        st.markdown('<div class="chat-interface">', unsafe_allow_html=True)
        if 'chat_history' not in st.session_state: st.session_state.chat_history = []
        for item in st.session_state.chat_history[-5:]:
            role = item.get('role','user') # Default to user for simplicity if role is missing
            text_content = item.get('text', item.get('question', item.get('response', '...')))
            if role == "user":
                st.markdown(f'<div class="chat-bubble user-bubble">{text_content}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-bubble ai-bubble">{text_content}</div>', unsafe_allow_html=True)

        user_query_ai = st.text_area("💬 Ask AI:", key="ai_chat_input_main_panel_v3", height=100)

        if st.button("🚀 Send to AI", key="send_ai_button_main_panel_v3", use_container_width=True):
            if st.session_state.get("openai_api_key") and user_query_ai:
                with st.spinner("🧠 AI processing..."):
                    current_slide_index = st.session_state.get('current_slide', 0)
                    slide_title = "General"
                    # Ensure slides_data is a list and current_slide_index is valid
                    if isinstance(slides_data, list) and slides_data and 0 <= current_slide_index < len(slides_data) and isinstance(slides_data[current_slide_index], dict) and 'title' in slides_data[current_slide_index]:
                        slide_title = slides_data[current_slide_index]['title']

                    filters = st.session_state.get('filters', {"year_range": (2010,2024), "analysis_type":"Complete Analysis", "time_horizon": "Current (2024)", "sectors": []}) # Provide default filters
                    ai_context = st.session_state.get("ai_context")
                    if not ai_context:
                        ai_context = get_enhanced_chart_context(slide_title, "Data for " + slide_title, filters)

                    response = chat_with_ai_enhanced(user_query_ai, ai_context)
                    st.session_state.chat_history.append({"role": "user", "text": user_query_ai, "timestamp": datetime.now().strftime("%H:%M")})
                    st.session_state.chat_history.append({"role": "ai", "text": response, "timestamp": datetime.now().strftime("%H:%M")})
                    st.rerun()
            elif not st.session_state.get("openai_api_key"): st.error("API Key needed.")
            else: st.warning("Enter a question.")
        st.markdown("</div>", unsafe_allow_html=True)
