#!/usr/bin/env python3
"""
GitHub Deployment Helper Script
Automates the process of uploading your project to GitHub for hosting
"""

import os
import subprocess
import sys
from pathlib import Path

def print_header():
    """Print welcome header"""
    print("\n" + "="*60)
    print("📤 GITHUB DEPLOYMENT HELPER")
    print("="*60)
    print("This script will help you upload your project to GitHub")
    print("for automatic deployment on Streamlit Cloud!")
    print("="*60 + "\n")

def check_git_installation():
    """Check if git is installed"""
    try:
        subprocess.run(['git', '--version'], capture_output=True, check=True)
        print("✅ Git is installed")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Git is not installed")
        print("Please install Git from: https://git-scm.com/downloads")
        return False

def initialize_repository():
    """Initialize git repository"""
    print("\n📋 Initializing Git repository...")
    
    if os.path.exists('.git'):
        print("  ✅ Git repository already exists")
        return True
    
    try:
        subprocess.run(['git', 'init'], check=True)
        print("  ✅ Git repository initialized")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to initialize repository: {e}")
        return False

def create_readme_for_github():
    """Create or update README for GitHub"""
    print("\n📝 Preparing README for GitHub...")
    
    # Use the AI_DASHBOARD_README.md as the main README
    if os.path.exists('AI_DASHBOARD_README.md'):
        try:
            # Copy AI_DASHBOARD_README.md to README.md for GitHub
            with open('AI_DASHBOARD_README.md', 'r') as src:
                content = src.read()
            
            with open('README.md', 'w') as dst:
                dst.write(content)
            
            print("  ✅ README.md updated for GitHub")
            return True
        except Exception as e:
            print(f"  ⚠️  Warning: Could not update README: {e}")
            return False
    else:
        print("  ⚠️  AI_DASHBOARD_README.md not found")
        return False

def add_files_to_git():
    """Add files to git"""
    print("\n📁 Adding files to Git...")
    
    # Files to definitely include
    important_files = [
        'interactive_ai_dashboard.py',
        'streamlit_requirements.txt',
        'README.md',
        'DEPLOYMENT_GUIDE.md',
        'FINAL_SUBMISSION_SUMMARY.md',
        'unified_reflection_essay.md',
        'data/processed/',
        'output/',
        '.gitignore'
    ]
    
    try:
        # Add all important files
        for file_path in important_files:
            if os.path.exists(file_path):
                subprocess.run(['git', 'add', file_path], check=True)
                print(f"  ✅ Added: {file_path}")
            else:
                print(f"  ⚠️  Not found: {file_path}")
        
        # Add any remaining Python files
        subprocess.run(['git', 'add', '*.py'], shell=True, check=False)
        subprocess.run(['git', 'add', '*.md'], shell=True, check=False)
        
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to add files: {e}")
        return False

def commit_changes():
    """Commit changes to git"""
    print("\n💾 Committing changes...")
    
    try:
        # Set user config if not set
        try:
            subprocess.run(['git', 'config', 'user.name'], capture_output=True, check=True)
        except subprocess.CalledProcessError:
            subprocess.run(['git', 'config', 'user.name', 'MSME Dashboard Creator'], check=True)
            subprocess.run(['git', 'config', 'user.email', 'dashboard@msme.ai'], check=True)
            print("  ✅ Git user configured")
        
        # Commit
        commit_message = "🚀 AI-Powered MSME Dashboard - Ready for deployment"
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print("  ✅ Changes committed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"  ❌ Failed to commit: {e}")
        return False

def display_github_instructions():
    """Display instructions for GitHub upload"""
    print("\n" + "="*60)
    print("📤 GITHUB UPLOAD INSTRUCTIONS")
    print("="*60)
    
    print("\n🌟 Your repository is ready! Now upload to GitHub:")
    
    print("\n📋 STEP-BY-STEP GITHUB SETUP:")
    print("\n1. 🌐 CREATE GITHUB REPOSITORY:")
    print("   → Go to: https://github.com/new")
    print("   → Repository name: msme-ai-dashboard")
    print("   → Description: AI-powered MSME ecosystem analysis dashboard")
    print("   → Make it PUBLIC (required for free hosting)")
    print("   → DO NOT initialize with README (we have one)")
    print("   → Click 'Create repository'")
    
    print("\n2. 📤 UPLOAD YOUR CODE:")
    print("   → Copy the commands GitHub shows you:")
    print("   → They will look like:")
    print("     git remote add origin https://github.com/YOURUSERNAME/msme-ai-dashboard.git")
    print("     git branch -M main")
    print("     git push -u origin main")
    
    print("\n3. ✅ VERIFY UPLOAD:")
    print("   → Refresh your GitHub repository page")
    print("   → You should see all your files")
    print("   → Check that README.md displays properly")
    
    print("\n4. 🚀 DEPLOY TO STREAMLIT:")
    print("   → Go to: https://share.streamlit.io")
    print("   → Sign in with GitHub")
    print("   → Click 'New app'")
    print("   → Select your repository: msme-ai-dashboard")
    print("   → Main file path: interactive_ai_dashboard.py")
    print("   → Click 'Deploy'")
    
    print("\n5. 🎉 GET YOUR LIVE URL:")
    print("   → Wait 2-3 minutes for deployment")
    print("   → Your URL: https://msme-ai-dashboard-YOURUSERNAME.streamlit.app")
    print("   → Add your OpenAI API key in the sidebar")
    print("   → Test the AI chat features")
    print("   → Share your live dashboard!")
    
    print("\n" + "="*60)
    print("🔑 DON'T FORGET:")
    print("   → Get OpenAI API key: https://platform.openai.com/api-keys")
    print("   → Add it to your dashboard sidebar after deployment")
    print("   → Test all features before submitting")
    print("="*60)

def display_quick_commands():
    """Display quick command reference"""
    print("\n📝 QUICK COMMAND REFERENCE:")
    print("\nIf you're comfortable with Git, here are the commands:")
    print("```")
    print("# After creating GitHub repository")
    print("git remote add origin https://github.com/YOURUSERNAME/msme-ai-dashboard.git")
    print("git branch -M main")
    print("git push -u origin main")
    print("```")
    
    print("\n🔄 TO UPDATE LATER:")
    print("```")
    print("git add .")
    print("git commit -m 'Update dashboard'")
    print("git push")
    print("```")

def main():
    """Main deployment preparation function"""
    print_header()
    
    try:
        # Check git installation
        if not check_git_installation():
            return
        
        # Initialize repository
        if not initialize_repository():
            return
        
        # Prepare README
        create_readme_for_github()
        
        # Add files
        if not add_files_to_git():
            return
        
        # Commit changes
        if not commit_changes():
            return
        
        # Show instructions
        display_github_instructions()
        display_quick_commands()
        
        print("\n🎯 NEXT: Create your GitHub repository and follow the upload instructions above!")
        
    except Exception as e:
        print(f"\n❌ Deployment preparation failed: {e}")
        print("Please check the error and try again.")

if __name__ == "__main__":
    main() 