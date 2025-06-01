import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv() # Load .env file

# API key should now be loaded into os.environ from the .env file
api_key = os.environ.get("OPENAI_API_KEY")

# --- IF YOU MUST HARDCODE FOR A QUICK TEST (NOT RECOMMENDED FOR LONG TERM): ---
# api_key = "sk-proj-....your-actual-key...."

if not api_key:
    print("Error: OPENAI_API_KEY environment variable not set.")
    print("Please set it or hardcode the key in the script (for testing only).")
    exit()

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