import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in environment.")

# Correct Gemini setup
genai.configure(api_key=api_key)

class GeminiClient:
    def __init__(self):
        # Ensure we're using the correct model name for the v1 API
        self.model = genai.GenerativeModel(model_name="gemini-pro")

    def get_response(self, prompt: str) -> str:
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error generating content: {e}"
