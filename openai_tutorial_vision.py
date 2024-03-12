from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import requests


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "gpt-4-vision-preview"

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-4-vision-preview",
  messages=[
    {
      "role": "user",
      "content": [
        {"type": "text", "text": "이 이미지는 무슨 내용이니?"},
        {
          "type": "image_url",
          "image_url": {
            "url": "https://jmagazine.joins.com/_data/photo/2017/12/thumb_237268740_xKqXAZdC_1.jpg",
          },
        },
      ],
    }
  ],
  max_tokens=300,
)

print(response.choices[0])