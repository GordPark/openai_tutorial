from dotenv import load_dotenv
import os
from openai import OpenAI
from PIL import Image
import requests

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
MODEL = "dall-e-3"

def generate_img(keyword):
    client = OpenAI(api_key=openai_api_key)
    # DALL-E에 이미지 생성 요청 보내기
    response = client.images.generate(
        model=MODEL,
        prompt=
        f"생성하려는 이미지는 {keyword}",
        size="1024x1024",
        quality="standard",
        n=1,

    )
    # 생성된 이미지 URL 가져오기
    image_url = response.data[0].url

    # 저장 파일 이름 설정
    filename = f"{keyword}.jpg"
    response_img = requests.get(image_url)
    with open(filename, 'wb') as f:
        f.write(response_img.content)
    
    return filename

def main():
    # 키워드 입력 받기
    keyword = input("키워드를 입력하세요: ")
   
    
    
    generate_img(keyword)


if __name__ == "__main__":
    main()



