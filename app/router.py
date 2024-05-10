from fastapi import APIRouter, File
from schema import CommonResponse, ErrorResponse

rScore = APIRouter(prefix="/py-api/score")

@rScore.post('/', tags = ['score'], response_model=CommonResponse)
async def upload_score(file: bytes = File()):
    # pdf 파일 받기

    # 받았다는 메시지 전송

    # 악보 인식

    # 악보 이미지 s3 저장

    # 반주 s3 저장
    
    return CommonResponse(success=True)

@rScore.get('/{team_id}', tags = ['score'], response_model=CommonResponse)
def get_scores():
    # 팀 아이디로 악보 조회
    return CommonResponse(success=True)

@rScore.delete('/{team_id}', tags = ['score'], response_model=CommonResponse)
def delete_scores():
    # 팀 아이디로 악보 조회
    return CommonResponse(success=True)
