import os
from typing import Dict, List

class Config:
    """Configuration class for the AI Text Analysis App"""
    
    # App Settings
    APP_NAME = "AI Text Analysis & Comparison"
    APP_VERSION = "1.0.0"
    DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'
    
    # Supported Image Formats
    SUPPORTED_IMAGE_FORMATS = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
    MAX_IMAGE_SIZE_MB = 10
    
    # API Configuration
    API_TIMEOUT = 30  # seconds
    MAX_RETRIES = 3
    
    # AI Models Configuration
    AI_MODELS = {
        'ChatGPT': {
            'name': 'ChatGPT',
            'provider': 'OpenAI',
            'model': 'gpt-4',
            'max_tokens': 1000,
            'temperature': 0.7,
            'system_prompt': 'You are a helpful assistant. Analyze the provided text and give a comprehensive response.',
            'enabled': True
        },
        'Gemini': {
            'name': 'Gemini',
            'provider': 'Google',
            'model': 'gemini-pro',
            'max_tokens': 1000,
            'temperature': 0.7,
            'system_prompt': 'You are a helpful assistant. Analyze the provided text and give a comprehensive response.',
            'enabled': True
        },
        'Grok': {
            'name': 'Grok',
            'provider': 'Groq',
            'model': 'mixtral-8x7b-32768',
            'max_tokens': 1000,
            'temperature': 0.7,
            'system_prompt': 'You are a helpful assistant. Analyze the provided text and give a comprehensive response.',
            'enabled': True
        },
        'Perplexity': {
            'name': 'Perplexity',
            'provider': 'Perplexity',
            'model': 'llama-3.1-sonar-small-128k-online',
            'max_tokens': 1000,
            'temperature': 0.7,
            'system_prompt': 'You are a helpful assistant. Analyze the provided text and give a comprehensive response.',
            'enabled': True
        },
        'DeepSeek': {
            'name': 'DeepSeek',
            'provider': 'DeepSeek',
            'model': 'deepseek-chat',
            'max_tokens': 1000,
            'temperature': 0.7,
            'system_prompt': 'You are a helpful assistant. Analyze the provided text and give a comprehensive response.',
            'enabled': True
        }
    }
    
    # API Endpoints
    API_ENDPOINTS = {
        'google_vision': 'https://vision.googleapis.com/v1/images:annotate',
        'openai': 'https://api.openai.com/v1/chat/completions',
        'google_generative': 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent',
        'groq': 'https://api.groq.com/openai/v1/chat/completions',
        'perplexity': 'https://api.perplexity.ai/chat/completions',
        'deepseek': 'https://api.deepseek.com/v1/chat/completions'
    }
    
    # Analysis Settings
    ANALYSIS_CONFIG = {
        'min_text_length': 10,
        'max_text_length': 10000,
        'similarity_threshold': 0.3,
        'quality_threshold': 0.5,
        'max_keywords': 10,
        'cache_enabled': True,
        'cache_ttl': 3600  # 1 hour
    }
    
    # UI Settings
    UI_CONFIG = {
        'theme': 'light',
        'sidebar_state': 'expanded',
        'page_title': '🔍 AI Text Analysis & Comparison',
        'page_icon': '🔍',
        'layout': 'wide'
    }
    
    # Error Messages
    ERROR_MESSAGES = {
        'no_api_key': 'API key not found. Please check your configuration.',
        'invalid_image': 'Invalid image format. Please upload a supported image type.',
        'text_extraction_failed': 'Failed to extract text from the image.',
        'api_request_failed': 'API request failed. Please check your internet connection and API keys.',
        'no_text_detected': 'No text detected in the image.',
        'processing_timeout': 'Processing timed out. Please try again.',
        'invalid_response': 'Invalid response from AI model.'
    }
    
    # Success Messages
    SUCCESS_MESSAGES = {
        'text_extracted': 'Text extracted successfully!',
        'analysis_complete': 'Analysis completed successfully!',
        'models_processed': 'All AI models processed successfully!'
    }
    
    @classmethod
    def get_api_key(cls, service: str) -> str:
        """Get API key for a specific service"""
        api_keys = {
            'google': os.getenv('GOOGLE_CLOUD_API_KEY'),
            'openai': os.getenv('OPENAI_API_KEY'),
            'anthropic': os.getenv('ANTHROPIC_API_KEY'),
            'groq': os.getenv('GROQ_API_KEY'),
            'perplexity': os.getenv('PERPLEXITY_API_KEY'),
            'deepseek': os.getenv('DEEPSEEK_API_KEY')
        }
        return api_keys.get(service.lower(), '')
    
    @classmethod
    def validate_config(cls) -> Dict[str, bool]:
        """Validate all configuration settings"""
        validation_results = {}
        
        # Check API keys
        for service in ['google', 'openai', 'anthropic', 'groq', 'perplexity', 'deepseek']:
            api_key = cls.get_api_key(service)
            validation_results[f'{service}_api_key'] = bool(api_key and api_key.strip())
        
        # Check required directories
        validation_results['temp_dir'] = os.path.exists('temp') if os.path.exists('temp') else True
        
        return validation_results
    
    @classmethod
    def get_enabled_models(cls) -> List[str]:
        """Get list of enabled AI models"""
        return [model_name for model_name, config in cls.AI_MODELS.items() 
                if config.get('enabled', True)]
    
    @classmethod
    def get_model_config(cls, model_name: str) -> Dict:
        """Get configuration for a specific model"""
        return cls.AI_MODELS.get(model_name, {})
    
    @classmethod
    def get_endpoint(cls, service: str) -> str:
        """Get API endpoint for a specific service"""
        return cls.API_ENDPOINTS.get(service.lower(), '')
    
    @classmethod
    def is_debug_mode(cls) -> bool:
        """Check if debug mode is enabled"""
        return cls.DEBUG
    
    @classmethod
    def get_supported_formats(cls) -> List[str]:
        """Get list of supported image formats"""
        return cls.SUPPORTED_IMAGE_FORMATS
    
    @classmethod
    def get_max_image_size(cls) -> int:
        """Get maximum image size in bytes"""
        return cls.MAX_IMAGE_SIZE_MB * 1024 * 1024 