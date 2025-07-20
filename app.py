import streamlit as st
import os
import io
from PIL import Image
import requests
from dotenv import load_dotenv
from openai import OpenAI
import re

# Load environment variables
load_dotenv()

# Set mobile-friendly page config
st.set_page_config(
    page_title="AI Image Q&A (OpenAI Only)",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="auto"
)

# Mobile-friendly custom CSS
st.markdown("""
<style>
    .stButton > button {
        font-size: 1.2rem;
        padding: 0.75em 2em;
        border-radius: 8px;
    }
    .stTextArea textarea {
        font-size: 1.1rem;
        min-height: 120px;
    }
    .block-container {
        max-width: 100vw !important;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    @media (max-width: 600px) {
        .stTextArea textarea {
            font-size: 1rem;
            min-height: 80px;
        }
        .stButton > button {
            font-size: 1rem;
            padding: 0.7em 1.2em;
        }
        h1, .stMarkdown h1 {
            font-size: 2rem !important;
        }
    }
</style>
""", unsafe_allow_html=True)

def clean_extracted_text(text):
    # Remove excessive whitespace and line breaks
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

class TextExtractor:
    def __init__(self):
        self.ocr_space_api_key = os.getenv('OCR_SPACE_API_KEY')

    def extract_text_from_image(self, image_bytes):
        try:
            url = "https://api.ocr.space/parse/image"
            files = {"filename": ("image.png", image_bytes)}
            data = {
                "apikey": self.ocr_space_api_key,
                "language": "eng",
            }
            response = requests.post(url, files=files, data=data)
            response.raise_for_status()
            result = response.json()
            if result.get("IsErroredOnProcessing"):
                st.error(f"OCR.Space error: {result.get('ErrorMessage')}")
                return None
            parsed_results = result.get("ParsedResults", [])
            if parsed_results and "ParsedText" in parsed_results[0]:
                return parsed_results[0]["ParsedText"]
            return "No text detected in the image (OCR.Space)."
        except Exception as e:
            st.error(f"Error extracting text with OCR.Space: {str(e)}")
            return None

class OpenAIModel:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None

    def answer_question(self, text):
        if not self.client:
            return "Error: OpenAI API key not configured."
        try:
            system_prompt = (
                "You are a helpful assistant. "
                "Given the following text extracted from an image, identify the main question. "
                "If the question has options (A, B, C, D, etc.), select the correct option and provide the answer in this format:\n"
                "Question: <the question>\n"
                "Option: <the selected option>\n"
                "Answer: <the answer>\n"
                "If there are no options, just provide:\n"
                "Question: <the question>\n"
                "Answer: <the answer>\n"
                "Be as concise and direct as possible. Only output the question, option (if any), and answer in the specified format."
            )
            completion = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": text}
                ]
            )
            return completion.choices[0].message.content
        except Exception as e:
            return f"Error: {str(e)}"

def main():
    st.markdown('<h1 style="text-align:center;">🤖 AI Image Q&A (OpenAI Only)</h1>', unsafe_allow_html=True)
    st.info("Upload an image containing questions. The app will extract the text and answer the questions using OpenAI.")

    text_extractor = TextExtractor()
    openai_model = OpenAIModel()

    st.sidebar.header("API Key Status")
    st.sidebar.write(f"{'✅' if openai_model.api_key else '❌'} OpenAI API Key")
    st.sidebar.write(f"{'✅' if text_extractor.ocr_space_api_key else '❌'} OCR.Space API Key")

    uploaded_file = st.file_uploader(
        "Choose an image file",
        type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
        help="Upload an image containing questions to extract and answer"
    )
    if uploaded_file is not None:
        uploaded_file.seek(0)
        image_bytes = uploaded_file.read()
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Uploaded Image", use_column_width=True)
        if st.button("🔍 Extract & Answer", type="primary"):
            with st.spinner("Extracting text from image..."):
                extracted_text = text_extractor.extract_text_from_image(image_bytes)
                if extracted_text:
                    cleaned_text = clean_extracted_text(extracted_text)
                    st.subheader("📝 Extracted Text")
                    st.text_area("Extracted Text", value=cleaned_text, height=200, disabled=True)
                    with st.spinner("Getting answer from OpenAI..."):
                        answer = openai_model.answer_question(cleaned_text)
                        st.subheader("🤖 OpenAI Answer")
                        st.markdown(f"<div style='font-size:1.2rem;word-break:break-word;'>{answer}</div>", unsafe_allow_html=True)
                else:
                    st.error("Failed to extract text from the image.")

if __name__ == "__main__":
    main() 