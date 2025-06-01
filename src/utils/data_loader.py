import pandas as pd
import os
import streamlit as st # For st.cache_data
from pathlib import Path

# It's good practice to ensure data files are found relative to the script or a known path
# For now, assume 'data/raw/wb_combined_indicators.csv' is accessible from where the main app runs.

@st.cache_data
def load_enhanced_msme_data():
    # Try to load the actual data file
    try:
        # Locate data file relative to this module's location (project root)
        base_dir = Path(__file__).resolve().parents[2]
        wb_data_path = base_dir / 'data' / 'raw' / 'wb_combined_indicators.csv'
        wb_data = pd.read_csv(wb_data_path)

        gdp_growth_2023 = wb_data[(wb_data['indicator'] == 'NY.GDP.MKTP.KD.ZG') & (wb_data['year'] == 2023)]['value'].iloc[0]
        labor_force_2024 = wb_data[(wb_data['indicator'] == 'SL.TLF.TOTL.IN') & (wb_data['year'] == 2024)]['value'].iloc[0] / 1000000
        exports_2023 = wb_data[(wb_data['indicator'] == 'NE.EXP.GNFS.ZS') & (wb_data['year'] == 2023)]['value'].iloc[0]
        unemployment_2024 = wb_data[(wb_data['indicator'] == 'SL.UEM.TOTL.ZS') & (wb_data['year'] == 2024)]['value'].iloc[0]

    except Exception as e:
        st.error(f"Error loading World Bank data from {wb_data_path}: {e}. Using fallback values.")
        gdp_growth_2023 = 8.15 # Fallback
        labor_force_2024 = 607.7 # Fallback
        exports_2023 = 21.85 # Fallback
        unemployment_2024 = 4.2 # Fallback

    years = list(range(2010, 2025))
    economic_data = pd.DataFrame({
        'Year': years,
        'GDP_Growth': [8.5, 5.24, 5.46, 6.39, 7.41, 8.0, 8.26, 6.79, 6.45, 3.87, -5.78, 9.69, 6.99, gdp_growth_2023 if 'gdp_growth_2023' in locals() else 7.2, 7.2], # Use loaded or fallback
        'Labor_Force_Million': [467.6, 471.9, 476.1, 484.5, 492.8, 500.8, 508.8, 516.8, 524.3, 531.4, 532.5, 550.4, 568.9, 589.0, labor_force_2024 if 'labor_force_2024' in locals() else 607.7],
        'Unemployment_Rate': [7.65, 7.62, 7.67, 7.71, 7.67, 7.63, 7.60, 7.62, 7.65, 6.51, 7.86, 6.38, 4.82, 4.17, unemployment_2024 if 'unemployment_2024' in locals() else 4.20],
        'Exports_Percent_GDP': [22.4, 24.54, 24.53, 25.43, 22.97, 19.81, 19.16, 18.79, 19.93, 18.66, 18.68, 21.40, 23.20, exports_2023 if 'exports_2023' in locals() else 21.85, 22.0],
        'FDI_Inflow_Billion': [27.4, 34.8, 28.2, 36.0, 55.5, 60.2, 43.5, 62.0, 50.6, 67.5, 82.0, 81.7, 71.4, 70.9, 83.5],
        'Digital_Adoption': [12, 15, 18, 22, 27, 33, 39, 45, 52, 58, 78, 82, 85, 87, 89],
        'MSME_Contribution_GDP': [29.7, 29.8, 29.9, 30.0, 30.1, 30.2, 30.3, 30.4, 30.5, 29.2, 29.5, 29.8, 30.1, 30.4, 30.7]
    })

    msme_sectors = pd.DataFrame({
        'Sector': ['Digital Commerce', 'Financial Services', 'Healthcare Tech', 'Agriculture Tech',
                  'Manufacturing', 'Education Tech', 'Renewable Energy', 'Food Processing'],
        'Growth_Potential': [18.5, 16.2, 14.8, 12.5, 15.2, 13.1, 11.8, 10.3],
        'Market_Size_Billion': [189, 156, 134, 98, 289, 76, 67, 143],
        'Employment_Multiplier': [6.8, 5.2, 4.5, 6.1, 4.4, 3.7, 2.9, 5.8],
        'Investment_Required': [45, 38, 42, 35, 67, 28, 89, 23],
        'Risk_Factor': [3.2, 2.8, 3.5, 4.1, 2.1, 3.8, 4.5, 2.3],
        'Digital_Readiness': [95, 87, 82, 68, 45, 92, 72, 56],
        'Export_Potential': [85, 72, 68, 78, 89, 65, 45, 82]
    })

    regional_data = pd.DataFrame({
        'State': ['Maharashtra', 'Gujarat', 'Tamil Nadu', 'Karnataka', 'Uttar Pradesh',
                 'Rajasthan', 'West Bengal', 'Andhra Pradesh', 'Telangana', 'Kerala'],
        'MSME_Count': [3712000, 1553000, 2174000, 1286000, 2028000, 1557000, 1234000, 967000, 845000, 734000],
        'GDP_Contribution': [14.2, 11.8, 10.4, 9.6, 8.2, 6.1, 5.8, 4.9, 4.3, 3.8],
        'Export_Share': [18.5, 16.2, 14.8, 12.3, 8.9, 7.2, 6.8, 5.4, 4.9, 4.2],
        'Digital_Score': [87, 82, 89, 91, 68, 72, 75, 78, 85, 83]
    })

    export_projection = pd.DataFrame({
        'Year': [2024, 2025, 2026, 2027, 2028, 2029, 2030],
        'Export_Percent_GDP': [exports_2023 if 'exports_2023' in locals() else 21.85, 22.1, 22.4, 22.7, 23.0, 23.3, 23.6],
        'MSME_Export_Share': [45.6, 46.5, 47.4, 48.3, 49.2, 50.1, 51.0],
        'Digital_Export_Growth': [15.2, 17.1, 19.2, 21.5, 24.0, 26.7, 29.6],
        'Traditional_Export_Growth': [8.5, 9.2, 9.8, 10.5, 11.1, 11.7, 12.3],
        'Services_Export_Share': [23.4, 24.1, 24.9, 25.8, 26.8, 27.9, 29.1]
    })

    return economic_data, msme_sectors, export_projection, regional_data
