# 🔍 AI Text Analysis & Comparison App

A comprehensive application that extracts text from images using Google Lens (Google Cloud Vision API) and then processes that text through multiple AI models for comparison and analysis.

## 🌟 Features

- **📸 Image Text Extraction**: Uses Google Cloud Vision API to extract text from uploaded images
- **🤖 Multi-AI Analysis**: Processes extracted text through 5 different AI models:
  - ChatGPT (OpenAI)
  - Gemini (Google)
  - Grok (via Groq)
  - Perplexity
  - DeepSeek
- **📊 Comparison Analysis**: Compares responses from all AI models
- **🎯 Consensus Generation**: Provides overall analysis and consensus
- **📈 Visual Analytics**: Interactive charts and metrics
- **🎨 Modern UI**: Beautiful, responsive interface built with Streamlit

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- API keys for the following services:
  - Google Cloud Vision API
  - OpenAI API
  - Anthropic API
  - Groq API
  - Perplexity API
  - DeepSeek API

### Installation

1. **Clone or download this project**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys**:
   - Copy `env_example.txt` to `.env`
   - Fill in your API keys:
   ```bash
   cp env_example.txt .env
   ```

4. **Edit the `.env` file** with your actual API keys:
   ```
   GOOGLE_CLOUD_API_KEY=your_actual_google_api_key
   OPENAI_API_KEY=your_actual_openai_api_key
   ANTHROPIC_API_KEY=your_actual_anthropic_api_key
   GROQ_API_KEY=your_actual_groq_api_key
   PERPLEXITY_API_KEY=your_actual_perplexity_api_key
   DEEPSEEK_API_KEY=your_actual_deepseek_api_key
   ```

5. **Run the application**:
   ```bash
   streamlit run app.py
   ```

6. **Open your browser** and navigate to `http://localhost:8501`

## 📋 How to Get API Keys

### Google Cloud Vision API
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing one
3. Enable the Cloud Vision API
4. Create credentials (API Key)
5. Copy the API key to your `.env` file

### OpenAI API (ChatGPT)
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Sign up or log in
3. Go to API Keys section
4. Create a new API key
5. Copy to your `.env` file

### Anthropic API (Claude)
1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Sign up or log in
3. Create an API key
4. Copy to your `.env` file

### Groq API
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up or log in
3. Generate an API key
4. Copy to your `.env` file

### Perplexity API
1. Go to [Perplexity API](https://www.perplexity.ai/api)
2. Sign up or log in
3. Get your API key
4. Copy to your `.env` file

### DeepSeek API
1. Visit [DeepSeek Platform](https://platform.deepseek.com/)
2. Sign up or log in
3. Generate an API key
4. Copy to your `.env` file

## 🎯 How to Use

1. **Upload an Image**: Click the upload area and select an image containing text
2. **Extract Text**: Click "Extract Text & Analyze" to process the image
3. **View Results**: The app will show:
   - Extracted text from the image
   - Individual responses from each AI model
   - Comparison analysis with similarity scores
   - Consensus summary

## 📊 Features Explained

### Individual Responses Tab
- View detailed responses from each AI model
- Compare different perspectives and insights
- Identify strengths and weaknesses of each model

### Comparison Analysis Tab
- Similarity score gauge showing agreement between models
- Common themes identified across all responses
- Visual representation of response characteristics

### Consensus Summary Tab
- Overall analysis combining insights from all models
- Response statistics and metrics
- Response length comparison chart

## 🔧 Customization

### Adding New AI Models
To add a new AI model, modify the `AIModels` class in `app.py`:

```python
def query_new_model(self, text):
    # Add your new model implementation here
    pass
```

### Modifying Analysis Parameters
Adjust the similarity analysis and consensus generation in the `ResultAnalyzer` class.

### UI Customization
Modify the CSS styles in the main function to customize the appearance.

## 🐛 Troubleshooting

### Common Issues

1. **API Key Errors**: Ensure all API keys are correctly set in the `.env` file
2. **Image Upload Issues**: Make sure the image format is supported (PNG, JPG, JPEG, GIF, BMP)
3. **Text Extraction Fails**: Check if the image contains clear, readable text
4. **Slow Response Times**: Some AI models may take longer to respond, especially during peak hours

### Error Messages

- **"No text detected"**: The image may not contain readable text or the text is too small/blurry
- **"API Error"**: Check your API key and internet connection
- **"Model Unavailable"**: The specific AI model may be temporarily unavailable

## 📝 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Support

If you encounter any issues or have questions, please open an issue on the project repository.

---

**Note**: This application requires valid API keys for all services to function properly. Make sure to keep your API keys secure and never commit them to version control. 