#!/bin/bash

# 🚀 AI-Powered MSME Analytics Platform - Launch Script
# This script launches the interactive dashboard locally

echo "🚀 Starting AI-Powered MSME Analytics Platform..."
echo "=================================================="

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.9+ and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ pip3 is not installed. Please install pip and try again."
    exit 1
fi

# Install requirements if they don't exist
echo "📦 Installing dependencies..."
pip3 install -r streamlit_requirements.txt

# Check if installation was successful
if [ $? -eq 0 ]; then
    echo "✅ Dependencies installed successfully!"
else
    echo "❌ Failed to install dependencies. Please check your internet connection and try again."
    exit 1
fi

echo ""
echo "🌟 Launching dashboard..."
echo "📍 Dashboard will open at: http://localhost:8501"
echo "🔑 Don't forget to add your OpenAI API key in the sidebar!"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

# Launch Streamlit
streamlit run interactive_ai_dashboard.py --server.port 8501 --server.address localhost

echo ""
echo "👋 Thanks for using the AI-Powered MSME Analytics Platform!"
