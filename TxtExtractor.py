import cv2
from doclayout_yolo import YOLOv10
import pytesseract
from pdf2image import convert_from_path
import numpy as np
import re
from prompt import ROLE,GOAL,BACKSTORY,DESCRIPTION,OUTCOME
from agent import Agents
from models import gemini_llm,llm

pytesseract.pytesseract.tesseract_cmd = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

images = convert_from_path(
    r"Factors_of_production.pdf"
)
txtfile = open('sample2.txt','a',encoding="utf-8")


for i,image in enumerate(images):

    img_np = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)

    # img = cv2.imread(img_np)

    title_txt = pytesseract.image_to_string(img_np,lang='eng+mal')

    cleaned_text = re.sub(r'[^A-Za-z0-9\s]+', '', title_txt)

    agent = Agents(gemini_llm,GOAL,ROLE,BACKSTORY,DESCRIPTION,OUTCOME,cleaned_text)

    result = agent.Builder()
    print(result.raw)
    print("---------------------------")
    txtfile.write(result.raw)
    txtfile.write("\n")
# print(cleaned_text)

