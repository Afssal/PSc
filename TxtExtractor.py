import cv2
from doclayout_yolo import YOLOv10
import pytesseract
from pdf2image import convert_from_path
import numpy as np
import re
from prompt import INSTRUCTION
from cleaner import LLm
from vectordb import collection
from ollama import chat
from ollama import ChatResponse


pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

images = convert_from_path(
    r"Factors_of_production.pdf"
)
txtfile = open('sample2.txt','a',encoding="utf-8")

ids = []
docs = []

for i,image in enumerate(images):

    img_np = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    # img = cv2.imread(img_np)

    title_txt = pytesseract.image_to_string(img_np,lang='eng+mal')

    cleaned_text = re.sub(r'[^A-Za-z0-9\s]+', '', title_txt)

    model = LLm(cleaned_text)

    result = model.Locallm()

    # agent = Agents(gemini_llm,GOAL,ROLE,BACKSTORY,DESCRIPTION,OUTCOME,cleaned_text)

    # result = agent.Builder()
    print(result)
    docs.append(result)
    ids.append(str(i))
    print("---------------------------")
    # txtfile.write(result)
    # txtfile.write("\n")
# print(cleaned_text)

collection.add(
    ids=ids,
    documents=docs
)

queries = input("Enter the question")

result = collection.query(
    query_texts=queries,
    n_results=5
)

print(result['documents'])

sample = f'''answer given question based on given contents
        content : {result['documents']} \n
        question : {queries}
        '''

response: ChatResponse = chat(model='llama3.2', messages=[
{
    'role': 'user',
    'content': sample,
},
])

print(response.message.content)

print("----------------------------------------")

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api = os.getenv('GEMINI_API_KEY')

client = genai.Client(api_key=gemini_api)

response = client.models.generate_content(model="gemini/gemini-2.5-flash-lit",contents=sample)

print(response.text)