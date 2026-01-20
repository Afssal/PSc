from ollama import chat
from ollama import ChatResponse
from google import genai
import os
from dotenv import load_dotenv
from prompt import INSTRUCTION

load_dotenv()

gemini_api = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=gemini_api)

class LLm:

    def __init__(self,query):

        self.query = INSTRUCTION + query


    def Locallm(self):

        response: ChatResponse = chat(model='llama3.2', messages=[
        {
            'role': 'user',
            'content': self.query,
        },
        ])

        return response.message.content
    

    def Gemini(self):

        response = client.models.generate_content(model="gemini/gemini-2.5-flash-lit",contents=self.query)

        return response.text