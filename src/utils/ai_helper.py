import streamlit as st # For session_state and secrets
import openai # For OpenAI client
import json # Though not used in current functions, good to keep if future AI responses are complex JSON
import httpx # Import httpx
import os # Import os to access environment variables

def get_enhanced_chart_context(chart_type, data_summary, filters):
    filter_context = f"""
    Applied Filters:
    - Year Range: {filters['year_range'][0]}-{filters['year_range'][1]}
    - Analysis Type: {filters['analysis_type']}
    - Time Horizon: {filters['time_horizon']}
    - Selected Sectors: {', '.join(filters['sectors']) if filters['sectors'] else 'All sectors'}
    """

    context = f"""
    You are an advanced AI analyst specializing in India's MSME (Micro, Small & Medium Enterprises) ecosystem.
    You have access to real-time data and can provide deep insights with specific recommendations.

    Current Analysis Context: {chart_type}
    Data Summary: {data_summary}
    {filter_context}

    Key Economic Indicators (EXACT World Bank Data - Unified Story Aligned):
    - India's GDP growth: 8.15% (2023, WB: 8.1529363109041) - EXACT from wb_combined_indicators.csv
    - Labor force: 607.7M workers (2024, WB: 607,691,498) - EXACT World Bank Official Data
    - MSME GDP contribution: 30.7% (2024 est.), stable at 29-30% range - MSME Ministry
    - Total MSME count: 57M+ registered enterprises (Dec 2024) - Udyam Portal
    - Export share: 21.85% of GDP (2023, WB: 21.8482115022381) - EXACT from World Bank

    Priority Growth Sectors (CORRECTED - Conservative Estimates):
    - Digital Commerce: 18.5% CAGR potential, $189B market - IBEF/McKinsey Reports
    - Financial Services: 16.2% CAGR, $156B market - Industry Analysis
    - Healthcare Tech: 14.8% CAGR, 4.5x employment multiplier - Sector Studies
    - Agriculture Tech: 12.5% CAGR, high rural impact - Government Reports

    Strategic Context (DATA SOURCES VERIFIED):
    - Digital adoption: 89% (2024) vs 12% (2010) - Estimated based on trends
    - FDI inflows: $83.5B (2024), steady growth - RBI Data
    - Export target: 23.6% of GDP by 2030 (current: 21.8%) - Conservative WB-aligned projection
    - Regional leaders: Maharashtra (3.7M), Tamil Nadu (2.2M), UP (2.0M) MSMEs - Udyam Data

    Provide actionable insights with specific numbers, policy recommendations,
    and investment strategies. Be conversational but data-driven.
    """
    return context

def chat_with_ai_enhanced(user_question, chart_context):
    try:
        # Prioritize environment variable (loaded from .env locally, or set in deployment)
        api_key = os.environ.get('OPENAI_API_KEY')
        
        # Fallback to st.secrets (for Streamlit Cloud)
        if not api_key and "OPENAI_API_KEY" in st.secrets:
            api_key = st.secrets["OPENAI_API_KEY"]
        
        # Fallback to session_state (if user manually entered, less ideal now)
        if not api_key and st.session_state.get('openai_api_key'):
            api_key = st.session_state.get('openai_api_key')

        if not api_key:
            return "⚠️ AI functionality requires an OpenAI API key. Please set it up in .env, Streamlit Cloud secrets, or enter it in the app."
        
        # Update session_state if a key was found from env or secrets, for consistency in UI
        if api_key and not st.session_state.get('openai_api_key'):
             st.session_state.openai_api_key = api_key

        client = openai.OpenAI(api_key=api_key)

        messages = [
            {"role": "system", "content": chart_context},
            {"role": "user", "content": user_question}
        ]

        chat_history = st.session_state.get('chat_history', [])
        for chat_item in chat_history[-2:]: # Iterate over a copy if modifying
            if isinstance(chat_item, dict) and 'question' in chat_item and 'response' in chat_item:
                 messages.insert(-1, {"role": "user", "content": chat_item["question"]})
                 messages.insert(-1, {"role": "assistant", "content": str(chat_item["response"])[:200] + "..."})
            elif isinstance(chat_item, tuple) and len(chat_item) == 2:
                 messages.insert(-1, {"role": "user", "content": str(chat_item[0])})
                 messages.insert(-1, {"role": "assistant", "content": str(chat_item[1])[:200] + "..."})

        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            max_tokens=600,
            temperature=0.7,
            presence_penalty=0.1,
            frequency_penalty=0.1
        )

        return response.choices[0].message.content

    except openai.APIError as e:
        st.error(f"OpenAI API Error: {e}")
        return f"❌ OpenAI API Error: {e}. Please check your API key and network."
    except Exception as e:
        st.error(f"Error in AI chat: {e}")
        return f"❌ Error: {str(e)}. Please try again."
