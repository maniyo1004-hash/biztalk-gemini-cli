# GEMINI.md - 업무 말투 변환기 (Business Tone Converter)

이 파일은 **업무 말투 변환기** 프로젝트의 컨텍스트와 개발 지침을 제공합니다. 이 저장소는 현재 프로젝트의 개요서와 제품 요구사항 명세서(PRD)를 포함하고 있으며, 실습을 위한 가이드 역할을 합니다.

## 1. 프로젝트 개요 (Project Overview)
- **목적**: 일상적인 말투를 상사, 고객, 동료 등 수신 대상에 맞는 정중하고 전문적인 업무 말투로 변환해주는 서비스입니다.
- **주요 기능**: 
  - 텍스트 입력 및 수신 대상(상사/타팀/고객/팀내) 선택
  - Upstage Solar-Pro2 LLM을 활용한 말투 변환
  - 변환 결과 출력 및 클립보드 복사
- **기술 스택**:
  - **백엔드**: Python 3.11+, FastAPI, LangChain, `langchain-upstage`
  - **프론트엔드**: Vanilla HTML, CSS, JavaScript (ES6+)
  - **AI**: Upstage Solar-Pro2 API
  - **배포**: Vercel (Frontend), Render/Railway (Backend)

## 2. 주요 파일 안내 (Key Files)
- **`개요서_업무말투변환기.md`**: 프로젝트의 배경, 목적, 핵심 기능 및 전체적인 흐름을 설명합니다.
- **`PRD_업무말투변환기.md`**: 상세 요구사항, 시스템 아키텍처, API 명세, 단계별 구현 가이드 및 프롬프트 예시를 포함한 핵심 문서입니다.
- **`my-rules.md`**: 이 프로젝트 내에서 Gemini CLI가 준수해야 할 한국어 응답 원칙, 보안 지침 및 금지 사항이 정의되어 있습니다.

## 3. 개발 및 실행 지침 (Development Guidelines)
현재 디렉토리는 문서 위주로 구성되어 있으며, 실제 구현 시 PRD의 **"7. 디렉토리 구조"** 및 **"9. 단계별 구현 가이드"**를 반드시 준수해야 합니다.

### 권장 개발 흐름 (Vibe Coding 원칙)
1. **완료 기준 정의**: 작업을 시작하기 전 PRD의 체크리스트를 확인합니다.
2. **조사 먼저, 구현 나중**: 새로운 라이브러리(예: LangChain Upstage) 연동 전, 사용법을 먼저 확인합니다.
3. **분석 먼저, 수정 나중**: 에러 발생 시 원인을 먼저 분석하고 수정을 진행합니다.
4. **코드 리뷰**: 구현 완료 후 전체 흐름을 다시 한번 복기합니다.

### 주요 명령어 (TODO: 구현 후 업데이트 필요)
- **백엔드 실행**: `cd backend && uvicorn main:app --reload`
- **패키지 설치**: `pip install -r backend/requirements.txt`
- **프론트엔드**: `frontend/index.html`을 브라우저에서 실행

## 4. Gemini CLI 설정
- **MCP 서버**: GitHub, Context7 (문서 검색), Playwright (웹 테스트) 서버가 설정되어 있습니다.
- **언어**: 모든 응답은 한국어로 진행합니다.
- **보안**: `.env` 파일 및 민감한 설정 파일은 절대 수정하거나 출력하지 않습니다.

---
*참고: 이 프로젝트는 바이브 코딩(Vibe Coding) 입문자를 위한 One Day 실습용으로 설계되었습니다.*

### Git Commit 과 Push는 반드시 허락을 받고 처리하세요. 
* 임의로 Remote Repository에 Push 하면 안됩니다.

### .env 환경변수 파일은 임의로 수정하면 안됩니다.

### Source를 변경한 이후에 관련된 PRD 문서의 내용도 반드시 업데이트 하세요.
* 완료 체크 리스트에 완료된 일들은 체크 표시를 하세요

