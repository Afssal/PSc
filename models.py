from crewai import LLM
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api = os.getenv('GEMINI_API_KEY')

llm = LLM(
    model="ollama/qwen3-vl:2b",
    base_url="http://localhost:11434"
)


gemini_llm = LLM(
    model="gemini/gemini-2.5-flash-lite",
    api_key=gemini_api,  
    temperature=0.7
)