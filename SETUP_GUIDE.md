# 🚀 Quick Setup Guide

## Prerequisites

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **API Keys** for the AI services you want to use

## 🎯 Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set Up API Keys
1. Copy `env_example.txt` to `.env`
2. Edit `.env` and add your API keys:
   ```
   GOOGLE_CLOUD_API_KEY=your_actual_google_api_key
   OPENAI_API_KEY=your_actual_openai_api_key
   ANTHROPIC_API_KEY=your_actual_anthropic_api_key
   GROQ_API_KEY=your_actual_groq_api_key
   PERPLEXITY_API_KEY=your_actual_perplexity_api_key
   DEEPSEEK_API_KEY=your_actual_deepseek_api_key
   ```

### Step 3: Run the App
```bash
streamlit run app.py
```

## 🔧 Alternative Ways to Run

### Windows Users
Double-click `run_app.bat` or run:
```cmd
run_app.bat
```

### Mac/Linux Users
```bash
./run_app.sh
```

### Test Your Setup
```bash
python test_setup.py
```

## 📋 Required API Keys

### Essential (for text extraction)
- **Google Cloud Vision API** - For extracting text from images

### AI Models (choose which ones you want)
- **OpenAI API** - For ChatGPT responses
- **Anthropic API** - For Claude responses  
- **Groq API** - For Grok responses
- **Perplexity API** - For Perplexity responses
- **DeepSeek API** - For DeepSeek responses

## 🔑 How to Get API Keys

### Google Cloud Vision API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the Cloud Vision API
4. Create credentials (API Key)

### OpenAI API (ChatGPT)
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up and go to API Keys
3. Create a new API key

### Anthropic API (Claude)
1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up and create an API key

### Groq API
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up and generate an API key

### Perplexity API
1. Go to [Perplexity API](https://www.perplexity.ai/api)
2. Sign up and get your API key

### DeepSeek API
1. Visit [DeepSeek Platform](https://platform.deepseek.com/)
2. Sign up and generate an API key

## 🎯 Minimum Setup

You can run the app with just **one API key**:
- **Google Cloud Vision API** (required for text extraction)
- Plus at least one AI model API key

The app will work with whatever API keys you provide!

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   ```bash
   pip install -r requirements.txt
   ```

2. **"API key not found" errors**
   - Check your `.env` file exists
   - Verify API keys are correct
   - Run `python test_setup.py` to test

3. **"Permission denied" on Mac/Linux**
   ```bash
   chmod +x run_app.sh
   ```

4. **App won't start**
   - Check if port 8501 is available
   - Try: `streamlit run app.py --server.port 8502`

### Test Your Setup
```bash
python test_setup.py
```

This will check:
- ✅ Python installation
- ✅ Required packages
- ✅ API key validity
- ✅ Environment setup

## 📱 Using the App

1. **Upload an image** containing text
2. **Click "Extract Text & Analyze"**
3. **View results** in three tabs:
   - Individual AI responses
   - Comparison analysis
   - Consensus summary

## 🎉 You're Ready!

Once you see the Streamlit interface, you're all set to start analyzing images with multiple AI models!

---

**Need help?** Check the main README.md for detailed documentation. 