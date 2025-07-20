#!/usr/bin/env python3
"""
Test script to verify API keys and setup for the AI Text Analysis App
"""

import os
import sys
import requests
from dotenv import load_dotenv
from config import Config

def test_api_key(service: str, api_key: str) -> bool:
    """Test if an API key is valid by making a simple request"""
    if not api_key or api_key.strip() == "":
        print(f"❌ {service}: No API key provided")
        return False
    
    if "your_" in api_key.lower() or "here" in api_key.lower():
        print(f"❌ {service}: API key appears to be a placeholder")
        return False
    
    try:
        # Simple test requests for each service
        if service.lower() == "google":
            # Test Google Cloud Vision API
            url = f"https://vision.googleapis.com/v1/images:annotate?key={api_key}"
            data = {
                "requests": [{
                    "image": {"content": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg=="},
                    "features": [{"type": "TEXT_DETECTION"}]
                }]
            }
            response = requests.post(url, json=data, timeout=10)
            if response.status_code == 200:
                print(f"✅ {service}: API key is valid")
                return True
            else:
                print(f"❌ {service}: API key validation failed (Status: {response.status_code})")
                return False
                
        elif service.lower() == "openai":
            # Test OpenAI API
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {"model": "gpt-3.5-turbo", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 5}
            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                print(f"✅ {service}: API key is valid")
                return True
            else:
                print(f"❌ {service}: API key validation failed (Status: {response.status_code})")
                return False
                
        elif service.lower() == "anthropic":
            # Test Anthropic API
            headers = {"x-api-key": api_key, "Content-Type": "application/json"}
            data = {"model": "claude-3-sonnet-20240229", "max_tokens": 5, "messages": [{"role": "user", "content": "Hello"}]}
            response = requests.post("https://api.anthropic.com/v1/messages", headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                print(f"✅ {service}: API key is valid")
                return True
            else:
                print(f"❌ {service}: API key validation failed (Status: {response.status_code})")
                return False
                
        elif service.lower() == "groq":
            # Test Groq API
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {"model": "mixtral-8x7b-32768", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 5}
            response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                print(f"✅ {service}: API key is valid")
                return True
            else:
                print(f"❌ {service}: API key validation failed (Status: {response.status_code})")
                return False
                
        elif service.lower() == "perplexity":
            # Test Perplexity API
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {"model": "llama-3.1-sonar-small-128k-online", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 5}
            response = requests.post("https://api.perplexity.ai/chat/completions", headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                print(f"✅ {service}: API key is valid")
                return True
            else:
                print(f"❌ {service}: API key validation failed (Status: {response.status_code})")
                return False
                
        elif service.lower() == "deepseek":
            # Test DeepSeek API
            headers = {"Authorization": f"Bearer {api_key}"}
            data = {"model": "deepseek-chat", "messages": [{"role": "user", "content": "Hello"}], "max_tokens": 5}
            response = requests.post("https://api.deepseek.com/v1/chat/completions", headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                print(f"✅ {service}: API key is valid")
                return True
            else:
                print(f"❌ {service}: API key validation failed (Status: {response.status_code})")
                return False
                
    except requests.exceptions.Timeout:
        print(f"❌ {service}: Request timed out")
        return False
    except requests.exceptions.RequestException as e:
        print(f"❌ {service}: Request failed - {str(e)}")
        return False
    except Exception as e:
        print(f"❌ {service}: Unexpected error - {str(e)}")
        return False

def test_dependencies():
    """Test if all required dependencies are installed"""
    print("🔍 Testing dependencies...")
    
    required_packages = [
        'streamlit', 'pillow', 'requests', 'google-cloud-vision',
        'openai', 'anthropic', 'groq',
        'python-dotenv', 'pandas', 'plotly', 'numpy'
    ]
    
    missing_packages = []
    
    # Custom import checks for packages with different import names
    import_checks = {
        'pillow': lambda: __import__('PIL.Image'),
        'google-cloud-vision': lambda: __import__('google.cloud.vision'),
        'python-dotenv': lambda: __import__('dotenv'),
    }

    for package in required_packages:
        try:
            if package in import_checks:
                import_checks[package]()
            else:
                __import__(package.replace('-', '_'))
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - Not installed")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n📦 Install missing packages with:")
        print(f"pip install {' '.join(missing_packages)}")
        return False
    
    print("✅ All dependencies are installed")
    return True

def test_environment():
    """Test environment setup"""
    print("\n🔍 Testing environment setup...")
    
    # Check if .env file exists
    if os.path.exists('.env'):
        print("✅ .env file found")
    else:
        print("❌ .env file not found")
        print("   Create a .env file with your API keys")
        return False
    
    # Load environment variables
    load_dotenv()
    
    # Test API keys (only for Google Cloud Vision, Gemini, and OpenAI)
    print("\n🔍 Testing API keys...")
    
    services = {
        'Google Cloud Vision': Config.get_api_key('google'),
        'Google Gemini': os.getenv('GOOGLE_GENAI_API_KEY'),
        'OpenAI (ChatGPT)': Config.get_api_key('openai'),
    }
    
    valid_keys = 0
    total_keys = len(services)
    
    for service, api_key in services.items():
        if service == 'Google Gemini':
            # Simple check for Gemini key presence
            if api_key and not api_key.lower().startswith('your_') and not api_key.lower().endswith('_here'):
                print(f"✅ {service}: API key is present")
                valid_keys += 1
            else:
                print(f"❌ {service}: API key appears to be a placeholder or missing")
        else:
            if test_api_key(service, api_key):
                valid_keys += 1
    
    print(f"\n📊 Summary: {valid_keys}/{total_keys} API keys are valid")
    
    if valid_keys == 0:
        print("\n❌ No valid API keys found. Please check your .env file.")
        return False
    elif valid_keys < total_keys:
        print(f"\n⚠️  Only {valid_keys} out of {total_keys} API keys are valid.")
        print("   The app will work with the available keys, but some features may be limited.")
    else:
        print("\n✅ All API keys are valid!")
    
    return True

def main():
    """Main test function"""
    print("🚀 AI Text Analysis App - Setup Test")
    print("=" * 50)
    
    # Test dependencies
    deps_ok = test_dependencies()
    
    if not deps_ok:
        print("\n❌ Please install missing dependencies before running the app.")
        sys.exit(1)
    
    # Test environment
    env_ok = test_environment()
    
    if not env_ok:
        print("\n❌ Environment setup failed. Please check your configuration.")
        sys.exit(1)
    
    print("\n✅ Setup test completed successfully!")
    print("\n🎉 You're ready to run the app!")
    print("   Run: streamlit run app.py")
    
    # Show next steps
    print("\n📋 Next steps:")
    print("1. Make sure you have at least one valid API key")
    print("2. Run: streamlit run app.py")
    print("3. Open your browser to http://localhost:8501")
    print("4. Upload an image and start analyzing!")

if __name__ == "__main__":
    main() 