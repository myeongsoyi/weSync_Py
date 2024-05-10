from pydantic import BaseModel
from typing import Optional

class ErrorResponse(BaseModel):
    errorCode: int
    errorMessage: str

class CommonResponse(BaseModel):
    success: bool
    data: Optional[dict] = None
    error: Optional[ErrorResponse] = None
    

class ScoreBase(BaseModel):
    position_id: int
    team_id: int
    title: str
    url: str

class ScoreCreate(ScoreBase):
    pass

class Score(ScoreBase):
    score_id: int

    class Config:
        orm_mode=True