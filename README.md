# Quantum MSME Analytics Dashboard

This project is a Streamlit-based interactive AI dashboard for analyzing India's MSME (Micro, Small & Medium Enterprises) ecosystem.

## Setup

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r streamlit_requirements.txt
    ```

4.  **Set up OpenAI API Key:**
    The application uses an OpenAI API key for its AI chat functionality. You can set this in one of two ways:
    *   **Secrets Management (Streamlit Sharing/Cloud):** If deploying to Streamlit Cloud, add your OpenAI API key as a secret named `OPENAI_API_KEY`.
    *   **Local Input:** When running locally, the application will prompt you to enter your OpenAI API key in the sidebar if it's not found in secrets.

## Running the Application

To run the Streamlit application locally, use the following command:

```bash
streamlit run interactive_ai_dashboard.py
```

Or, if you are using the `launch.sh` script:

```bash
bash launch.sh
```

The application should open in your default web browser.

## Files for Deployment

*   `interactive_ai_dashboard.py`: The main Streamlit application file.
*   `streamlit_requirements.txt`: Contains the Python package dependencies.
*   `launch.sh`: (Optional) A shell script that can be used to launch the application, potentially with specific configurations.
*   `data/`: This directory should contain necessary data files, such as `data/raw/wb_combined_indicators.csv`.
*   `output/images/`: This directory should contain any static images used by the dashboard, like chapter visualizations.

Make sure these files and directories are pushed to your GitHub repository for Streamlit Cloud deployment. 