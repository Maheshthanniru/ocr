import re
import hashlib
import json
from typing import Dict, List, Optional, Tuple
import requests
from datetime import datetime

class TextProcessor:
    """Utility class for text processing and analysis"""
    
    @staticmethod
    def clean_text(text: str) -> str:
        """Clean and normalize extracted text"""
        if not text:
            return ""
        
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text.strip())
        
        # Remove special characters but keep punctuation
        text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)]', '', text)
        
        return text
    
    @staticmethod
    def extract_keywords(text: str, max_keywords: int = 10) -> List[str]:
        """Extract key words from text"""
        if not text:
            return []
        
        # Remove common stop words
        stop_words = {
            'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
            'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have',
            'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should',
            'may', 'might', 'can', 'this', 'that', 'these', 'those', 'i', 'you',
            'he', 'she', 'it', 'we', 'they', 'me', 'him', 'her', 'us', 'them'
        }
        
        # Split text into words and filter
        words = re.findall(r'\b\w+\b', text.lower())
        words = [word for word in words if word not in stop_words and len(word) > 3]
        
        # Count word frequency
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1
        
        # Return top keywords
        sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
        return [word for word, freq in sorted_words[:max_keywords]]
    
    @staticmethod
    def calculate_text_similarity(text1: str, text2: str) -> float:
        """Calculate similarity between two texts using Jaccard similarity"""
        if not text1 or not text2:
            return 0.0
        
        # Convert to sets of words
        words1 = set(re.findall(r'\b\w+\b', text1.lower()))
        words2 = set(re.findall(r'\b\w+\b', text2.lower()))
        
        if not words1 or not words2:
            return 0.0
        
        # Calculate Jaccard similarity
        intersection = len(words1.intersection(words2))
        union = len(words1.union(words2))
        
        return intersection / union if union > 0 else 0.0

class APIHandler:
    """Utility class for API request handling and error management"""
    
    @staticmethod
    def make_api_request(url: str, headers: Dict, data: Dict, timeout: int = 30) -> Tuple[bool, str]:
        """Make API request with error handling"""
        try:
            response = requests.post(url, headers=headers, json=data, timeout=timeout)
            response.raise_for_status()
            return True, response.json()
        except requests.exceptions.Timeout:
            return False, "Request timed out"
        except requests.exceptions.RequestException as e:
            return False, f"Request failed: {str(e)}"
        except json.JSONDecodeError:
            return False, "Invalid JSON response"
        except Exception as e:
            return False, f"Unexpected error: {str(e)}"
    
    @staticmethod
    def validate_api_key(api_key: str) -> bool:
        """Validate if API key is properly formatted"""
        if not api_key or api_key.strip() == "":
            return False
        
        # Basic validation - check if it's not the placeholder
        if "your_" in api_key.lower() or "here" in api_key.lower():
            return False
        
        return True

class DataAnalyzer:
    """Utility class for analyzing AI response data"""
    
    @staticmethod
    def analyze_response_quality(responses: Dict[str, str]) -> Dict[str, float]:
        """Analyze the quality of AI responses"""
        quality_scores = {}
        
        for model, response in responses.items():
            if not response or response.startswith("Error:"):
                quality_scores[model] = 0.0
                continue
            
            # Calculate quality score based on multiple factors
            score = 0.0
            
            # Length factor (not too short, not too long)
            length = len(response)
            if 100 <= length <= 2000:
                score += 0.3
            elif 50 <= length <= 5000:
                score += 0.2
            
            # Structure factor (check for paragraphs, bullet points, etc.)
            if '\n\n' in response or '•' in response or '-' in response:
                score += 0.2
            
            # Content factor (check for meaningful words)
            meaningful_words = len([word for word in response.split() if len(word) > 4])
            if meaningful_words > 10:
                score += 0.3
            
            # Completeness factor (check for question marks, indicating incomplete thoughts)
            if response.endswith('?') and response.count('?') == 1:
                score -= 0.1
            
            quality_scores[model] = min(1.0, max(0.0, score))
        
        return quality_scores
    
    @staticmethod
    def generate_response_summary(responses: Dict[str, str]) -> Dict[str, any]:
        """Generate a comprehensive summary of all responses"""
        valid_responses = {k: v for k, v in responses.items() 
                          if v and not v.startswith("Error:")}
        
        if not valid_responses:
            return {
                "total_models": len(responses),
                "successful_responses": 0,
                "failed_responses": len(responses),
                "average_length": 0,
                "common_themes": [],
                "consensus_level": "none"
            }
        
        # Calculate statistics
        lengths = [len(resp) for resp in valid_responses.values()]
        avg_length = sum(lengths) / len(lengths)
        
        # Extract common themes
        all_text = " ".join(valid_responses.values())
        common_themes = TextProcessor.extract_keywords(all_text, 5)
        
        # Determine consensus level
        if len(valid_responses) == len(responses):
            consensus_level = "high"
        elif len(valid_responses) >= len(responses) * 0.7:
            consensus_level = "moderate"
        else:
            consensus_level = "low"
        
        return {
            "total_models": len(responses),
            "successful_responses": len(valid_responses),
            "failed_responses": len(responses) - len(valid_responses),
            "average_length": avg_length,
            "common_themes": common_themes,
            "consensus_level": consensus_level
        }

class CacheManager:
    """Simple cache manager for storing API responses"""
    
    def __init__(self):
        self.cache = {}
    
    def get_cache_key(self, text: str, model: str) -> str:
        """Generate cache key for text and model combination"""
        text_hash = hashlib.md5(text.encode()).hexdigest()
        return f"{model}_{text_hash}"
    
    def get(self, text: str, model: str) -> Optional[str]:
        """Get cached response"""
        key = self.get_cache_key(text, model)
        return self.cache.get(key)
    
    def set(self, text: str, model: str, response: str):
        """Cache response"""
        key = self.get_cache_key(text, model)
        self.cache[key] = response
    
    def clear(self):
        """Clear all cached data"""
        self.cache.clear()

class Logger:
    """Simple logging utility"""
    
    @staticmethod
    def log_api_call(model: str, success: bool, error_message: str = ""):
        """Log API call results"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        status = "SUCCESS" if success else "FAILED"
        log_entry = f"[{timestamp}] {model}: {status}"
        
        if error_message:
            log_entry += f" - {error_message}"
        
        print(log_entry)
    
    @staticmethod
    def log_analysis(text_length: int, models_used: int, processing_time: float):
        """Log analysis session statistics"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"[{timestamp}] ANALYSIS: Text length={text_length}, Models={models_used}, Time={processing_time:.2f}s"
        print(log_entry) 