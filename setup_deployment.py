#!/usr/bin/env python3
"""
AI-Powered MSME Dashboard - Deployment Setup Script
This script helps prepare your project for deployment with minimal effort.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def print_header():
    """Print welcome header"""
    print("\n" + "="*60)
    print("🚀 AI-POWERED MSME DASHBOARD DEPLOYMENT SETUP")
    print("="*60)
    print("This script will help you deploy your interactive dashboard")
    print("with OpenAI integration for FREE on Streamlit Cloud!")
    print("="*60 + "\n")

def check_requirements():
    """Check if required packages are installed"""
    print("📋 Checking requirements...")
    
    required_packages = [
        'streamlit', 'plotly', 'pandas', 'numpy', 'openai'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} (missing)")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n⚠️  Missing packages: {', '.join(missing_packages)}")
        print("Installing missing packages...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install'] + missing_packages)
        print("✅ All packages installed!")
    else:
        print("\n✅ All required packages are installed!")

def create_directory_structure():
    """Create proper directory structure"""
    print("\n📁 Creating directory structure...")
    
    directories = [
        'data/processed',
        'data/raw', 
        'output/images',
        'output/reports',
        'assets'
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"  ✅ Created: {directory}")

def copy_existing_files():
    """Copy existing analysis files to proper locations"""
    print("\n📄 Organizing existing files...")
    
    # Map of source files to destination paths
    file_mappings = {
        'unified_msme_story.py': 'data/processed/',
        'unified_reflection_essay.md': 'output/reports/',
        'chapter1_economic_foundation.png': 'output/images/',
        'chapter2_msme_opportunities.png': 'output/images/',
        'chapter3_export_pathway.png': 'output/images/',
        'unified_msme_story.md': 'output/reports/'
    }
    
    for source, dest_dir in file_mappings.items():
        if os.path.exists(source):
            shutil.copy2(source, dest_dir)
            print(f"  ✅ Moved: {source} → {dest_dir}")
        else:
            print(f"  ⚠️  Not found: {source}")

def generate_git_files():
    """Generate .gitignore and other git files"""
    print("\n📝 Creating Git configuration files...")
    
    gitignore_content = """
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Streamlit
.streamlit/

# API Keys and secrets
.env
config.py
secrets.toml

# Data files (if too large)
data/raw/*.csv
data/raw/*.json
data/raw/*.xlsx
*.db

# Temporary files
*.tmp
*.log
"""
    
    with open('.gitignore', 'w') as f:
        f.write(gitignore_content.strip())
    print("  ✅ Created .gitignore")

def create_launch_script():
    """Create a local launch script"""
    print("\n🔧 Creating launch script...")
    
    launch_script = """#!/bin/bash
# Local development launcher
echo "🚀 Starting MSME AI Dashboard..."
echo "📍 Dashboard will be available at: http://localhost:8501"
echo "🔑 Don't forget to add your OpenAI API key in the sidebar!"
echo ""

streamlit run interactive_ai_dashboard.py
"""
    
    with open('launch.sh', 'w') as f:
        f.write(launch_script)
    
    # Make executable on Unix systems
    if os.name != 'nt':
        os.chmod('launch.sh', 0o755)
    
    print("  ✅ Created launch.sh")

def display_next_steps():
    """Display next steps for deployment"""
    print("\n" + "="*60)
    print("🎉 SETUP COMPLETE!")
    print("="*60)
    
    print("\n📋 NEXT STEPS:")
    print("\n1. 🔑 GET OPENAI API KEY:")
    print("   → Visit: https://platform.openai.com/api-keys")
    print("   → Create new secret key")
    print("   → Copy the key for use in the dashboard")
    
    print("\n2. 🧪 TEST LOCALLY:")
    print("   → Run: python setup_deployment.py --test")
    print("   → Or run: streamlit run interactive_ai_dashboard.py")
    print("   → Open: http://localhost:8501")
    
    print("\n3. 📤 DEPLOY TO GITHUB:")
    print("   → Create new repository on GitHub")
    print("   → Upload all files to the repository")
    print("   → Make repository PUBLIC (required for free hosting)")
    
    print("\n4. 🌐 DEPLOY TO STREAMLIT CLOUD:")
    print("   → Visit: https://share.streamlit.io")
    print("   → Sign in with GitHub")
    print("   → Click 'New app'")
    print("   → Select your repository")
    print("   → Set main file: interactive_ai_dashboard.py")
    print("   → Click 'Deploy'")
    
    print("\n5. ✅ SHARE YOUR DASHBOARD:")
    print("   → Get your URL: https://your-app-name.streamlit.app")
    print("   → Share with stakeholders!")
    
    print("\n" + "="*60)
    print("📚 HELPFUL RESOURCES:")
    print("   → Deployment Guide: DEPLOYMENT_GUIDE.md")
    print("   → Project README: AI_DASHBOARD_README.md") 
    print("   → Streamlit Docs: https://docs.streamlit.io")
    print("   → OpenAI API Docs: https://platform.openai.com/docs")
    print("="*60)

def test_dashboard():
    """Test the dashboard locally"""
    print("\n🧪 Testing dashboard locally...")
    
    if not os.path.exists('interactive_ai_dashboard.py'):
        print("❌ interactive_ai_dashboard.py not found!")
        return False
    
    try:
        # Try to import and basic validation
        print("  📋 Checking dashboard file...")
        with open('interactive_ai_dashboard.py', 'r') as f:
            content = f.read()
            if 'streamlit' in content and 'openai' in content:
                print("  ✅ Dashboard file looks good!")
            else:
                print("  ⚠️  Dashboard file might have issues")
        
        print("\n🚀 Starting local test server...")
        print("📍 Dashboard will open at: http://localhost:8501")
        print("🔑 Add your OpenAI API key in the sidebar to test AI features")
        print("\n⏹️  Press Ctrl+C to stop the server")
        
        # Launch Streamlit
        subprocess.run([sys.executable, '-m', 'streamlit', 'run', 'interactive_ai_dashboard.py'])
        
    except KeyboardInterrupt:
        print("\n✅ Test completed!")
    except Exception as e:
        print(f"❌ Error running test: {e}")

def main():
    """Main setup function"""
    print_header()
    
    # Check command line arguments
    if len(sys.argv) > 1 and sys.argv[1] == '--test':
        test_dashboard()
        return
    
    try:
        check_requirements()
        create_directory_structure()
        copy_existing_files()
        generate_git_files()
        create_launch_script()
        display_next_steps()
        
        print("\n🎯 Want to test locally? Run: python setup_deployment.py --test")
        
    except Exception as e:
        print(f"\n❌ Setup failed: {e}")
        print("Please check the error and try again.")

if __name__ == "__main__":
    main() 