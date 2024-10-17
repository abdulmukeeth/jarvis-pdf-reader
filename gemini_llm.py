import os
from typing import Optional, List
from langchain.llms.base import LLM
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class GeminiLLM(LLM):
    """
    Custom LangChain LLM wrapper for Google Gemini.
    """

    model_name: str = "gemini-1.5-flash" 
    api_key: Optional[str] = None

    @property
    def _llm_type(self) -> str:
        return "gemini"

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        # Configure the Gemini API key
        genai.configure(api_key=self.api_key or os.getenv("GEMINI_API_KEY"))

        # Initialize the Gemini model
        model = genai.GenerativeModel(self.model_name)

        # Generate content based on the prompt
        response = model.generate_content(prompt)
        generated_text = response.text

        # Handle stop sequences if provided
        if stop:
            for stop_seq in stop:
                index = generated_text.find(stop_seq)
                if index != -1:
                    generated_text = generated_text[:index]
        return generated_text

    @property
    def _identifying_params(self) -> dict:
        return {"model_name": self.model_name}

