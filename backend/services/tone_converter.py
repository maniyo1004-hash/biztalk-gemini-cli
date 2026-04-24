import os
from dotenv import load_dotenv
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from prompts.templates import PROMPTS

load_dotenv()

class ToneConverter:
    def __init__(self):
        api_key = os.getenv("UPSTAGE_API_KEY")
        if not api_key:
            raise ValueError("UPSTAGE_API_KEY is not set in environment variables.")
        
        # PRD 명세에 따라 solar-pro 모델 사용
        self.llm = ChatUpstage(model="solar-pro", upstage_api_key=api_key)

    async def convert(self, text: str, target_audience: str) -> str:
        if target_audience not in PROMPTS:
            raise ValueError(f"Invalid target audience: {target_audience}")

        system_prompt = PROMPTS[target_audience]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "{text}")
        ])

        # LangChain LCEL 방식 사용
        chain = prompt | self.llm
        
        try:
            response = await chain.ainvoke({"text": text})
            return response.content
        except Exception as e:
            # 로깅이나 추가 에러 처리가 필요할 수 있음
            raise RuntimeError(f"Error calling Upstage API: {str(e)}")

# 싱글톤 패턴으로 인스턴스 제공
tone_converter = ToneConverter()
