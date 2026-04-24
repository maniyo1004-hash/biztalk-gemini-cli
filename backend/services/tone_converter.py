import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from prompts.templates import PROMPTS

# .env 파일 로드 (backend/.env 확인)
load_dotenv()

class ToneConverter:
    def __init__(self):
        api_key = os.getenv("UPSTAGE_API_KEY")
        if not api_key:
            # 환경 변수가 로드되지 않았을 경우를 대비해 다시 한 번 시도
            load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))
            api_key = os.getenv("UPSTAGE_API_KEY")
            
        if not api_key:
            raise ValueError("UPSTAGE_API_KEY is not set in environment variables.")
        
        # Upstage는 OpenAI 호환 API를 제공하므로 ChatOpenAI 사용 가능
        self.llm = ChatOpenAI(
            model="solar-pro", 
            openai_api_key=api_key,
            base_url="https://api.upstage.ai/v1/solar"
        )

    async def convert(self, text: str, target_audience: str) -> str:
        if target_audience not in PROMPTS:
            raise ValueError(f"Invalid target audience: {target_audience}")

        system_prompt = PROMPTS[target_audience]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{text}")
        ])

        chain = prompt | self.llm
        
        try:
            # invoke를 awaitable하게 사용 (ainvoke)
            response = await chain.ainvoke({"text": text})
            return response.content
        except Exception as e:
            raise RuntimeError(f"Error calling Upstage API: {str(e)}")

# 싱글톤 패턴으로 인스턴스 제공
tone_converter = ToneConverter()
