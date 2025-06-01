import os
import pytest
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load .env file

# Skip entire test module if OPENAI_API_KEY is not set
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    pytest.skip("Skipping OpenAI connection test: OPENAI_API_KEY not set", allow_module_level=True)

# API key should now be loaded into os.environ from the .env file
# Now that module-level skip is in place, api_key is guaranteed to be set
# --- IF YOU MUST HARDCODE FOR A QUICK TEST (NOT RECOMMENDED FOR LONG TERM): ---
# api_key = "sk-proj-....your-actual-key...."

print(f"Attempting to connect to OpenAI with key: {api_key[:10]}...{api_key[-4:]}")

try:
    client = OpenAI(api_key=api_key)
    
    print("OpenAI client initialized successfully.")
    
    print("Attempting to list models...")
    models = client.models.list()
    
    print("Successfully connected to OpenAI and fetched models.")
    print("First few models:")
    for i, model in enumerate(models.data):
        if i < 5:
            print(f"- {model.id}")
        else:
            break
    print("\nTest completed successfully!")

except Exception as e:
    print(f"\nAn error occurred: {e}")
    print("Please check your API key, network connection, and OpenAI account status.") 