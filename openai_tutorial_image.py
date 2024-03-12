from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import requests


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "dall-e-3"

client = OpenAI(api_key=openai_api_key)

response = client.images.generate(
    model=MODEL,
    prompt=
    "유명한 인상파화가가 그린 지구인데 우주에서 본 시점으로 지구안에는 물이 가득차 있고 모양은 시계처럼 그리고 산들은 입체감이 있게 그려줘",
    size="1024x1024",
    quality="standard",
    n=1,

)

image_url = response.data[0].url

# 저장 파일 이름 설정
filename = "image.jpg"
response_img = requests.get(image_url)
with open(filename, 'wb') as f:
    f.write(response_img.content)
Image.open(filename)