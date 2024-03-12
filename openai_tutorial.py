from dotenv import load_dotenv  # 환경 변수 파일을 로드하기 위한 도구제공
import os   # 운영체제와 상호작용하기 위한 여러 함수 제공
from openai import OpenAI   # 오픈AI API사용하기 위해 import

load_dotenv()   # 프로젝트 디렉토리에서 .env 파일을 로드 후 환경 변수 설정

openai_api_key = os.getenv("OPENAI_API_KEY") # .env 파일에서 OPENAI_API_KEY 환경 변수 값 가져옴


MODEL="gpt-3.5-turbo" # 사용할 OpenAI 모델의 이름 지정
client = OpenAI(api_key=openai_api_key) # OpenAI 클래스의 API 키를 인자로 전달 후 OpenAI 클라이언트를 초기화

response = client.chat.completions.create( # 챗봇의 대화를 생성
  model=MODEL, # 사용할 OpenAI 모델 이름을 지정
  messages=[ # 대화의 각 메시지를 포함하는 리스트
      # role은 "system", "user", "assistant" 중 하나로 지정
      # 시스템 메시지, 사용자 메시지, 보조 메시지
      # content는 해당 메시지의 내용
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    # {"role": "user", "content": "Where was it played?"}
  ]
)
print(response.choices[0].message.content) # 서버에서 반환된 응답 중에서 생성된 대화의 첫 번째 메시지를 출력
# JSON 형식으로, choices 배열에 대화의 각 단계에 대한 정보가 포함
pass