from fastapi import FastAPI
from pydantic import BaseModel
from nlp_utils import simplify_text, detect_mood
from recommender import BookRecommender
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

class TextRequest(BaseModel):
    text: str

class MoodRequest(BaseModel):
    mood: str

# Initialize book recommender
recommender = BookRecommender("books.csv")

@app.post("/simplify_text")
async def simplify_text_endpoint(req: TextRequest):
    summary = simplify_text(req.text)
    return {"summary": summary}

@app.post("/detect_mood")
async def detect_mood_endpoint(req: TextRequest):
    mood = detect_mood(req.text)
    return {"mood": mood}

@app.post("/recommend_books")
async def recommend_books_endpoint(req: MoodRequest):
    books = recommender.recommend(req.mood)
    return books
