from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from app import crud, database, models, schema
from app.router import rScore

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rScore)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    database.create_tables()

# @app.get("/")
# async def root():
#     return RedirectResponse(url="/api/scores/")

# @app.get("/api/scores/")
# async def get_scores(db: Session = Depends(get_db)):
#     scores = crud.get_scores(db)
#     return scores

# @app.get("/api/scores/{score_id}")
# async def get_score(score_id: int, db: Session = Depends(get_db)):
#     score = crud.get_score(db, score_id)
#     if score is None:
#         raise HTTPException(status_code=404, detail="Score not found")
#     return score

# @app.post("/api/scores/")
# async def create_score(score: schema.ScoreCreate, db: Session = Depends(get_db)):
#     db_score = crud.create_score(db, score)
#     return db_score

# @app.put("/api/scores/{score_id}")
# async def update_score(score_id: int, updated_score: schema.ScoreCreate, db: Session = Depends(get_db)):
#     db_score = crud.get_score(db, score_id)
#     if db_score is None:
#         raise HTTPException(status_code=404, detail="Score not found")
#     updated_score = crud.update_score(db, db_score, updated_score)
#     return updated_score

# @app.delete("/api/scores/{score_id}")
# async def delete_score(score_id: int, db: Session = Depends(get_db)):
#     db_score = crud.get_score(db, score_id)
#     if db_score is None:
#         raise HTTPException(status_code=404, detail="Score not found")
#     crud.delete_score(db, db_score)
#     return {"message": "Score deleted successfully"}
