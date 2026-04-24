from fastapi import APIRouter, HTTPException
from models.schemas import ConvertRequest, ConvertResponse
from services.tone_converter import tone_converter

router = APIRouter()

@router.post("/convert", response_model=ConvertResponse)
async def convert_text(request: ConvertRequest):
    if not request.text.strip():
        raise HTTPException(status_code=422, detail="text 필드는 필수이며 비어있을 수 없습니다.")
    
    try:
        converted_text = await tone_converter.convert(
            text=request.text,
            target_audience=request.target_audience
        )
        
        return ConvertResponse(
            converted_text=converted_text,
            target_audience=request.target_audience,
            original_text=request.text
        )
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"말투 변환 중 오류가 발생했습니다: {str(e)}")
