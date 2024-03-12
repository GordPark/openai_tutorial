from dotenv import load_dotenv
import os
from openai import OpenAI


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

response = client.chat.completions.create(
  model="gpt-3.5-turbo-0125",
  response_format={ "type": "json_object" }, # 서버에서 반환되는 응답의 형식(JSON 객체)을 지정
  messages=[
    {"role": "system", "content": "너는 고객의 만족도를 분석하는 로봇이야. 고객의 응답내용을 토대로 만족 또는 불만족인지 구분해줘 You are a helpful assistant designed to output JSON."},
    # to output JSON : API에 JSON형식으로 대답을 요구해야 오류가 나지않음
    {"role": "user", "content": "오늘 구매한 컴퓨터는 소음이 심하고 가격에 비해서 느린것 같아"}
    # # 어시스턴트의 응답은 API 호출로 생성
  ]
) 🚨📢
print(response.choices[0].message.content)
pass