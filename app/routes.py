from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas import FeedbackRequest, FeedbackResponse
from app.models import Feedback
from app.database import SessionLocal
from openai import OpenAI
import os

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

client = OpenAI()

from fastapi import HTTPException

@router.post("/feedback", response_model=FeedbackResponse)
def generate_feedback(data: FeedbackRequest, db: Session = Depends(get_db)):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are an experienced HR professional and writing coach.
                    Your job is to take raw, unstructured performance feedback and transform it into a clear, professional, and detailed summary.
                    Expand on vague phrases, organize thoughts into coherent points, and use professional tone suitable for performance reviews.
                    Avoid repetition, and ensure the summary sounds complete and polished while staying true to the original meaning.
                    """
                },
                {
                    "role": "user",
                    "content": data.raw_input
                }
            ]
        )
        summary = response.choices[0].message.content
    except Exception as e:
        print("❌ OpenAI API Error:", str(e))
        raise HTTPException(status_code=500, detail="LLM call failed")

    record = Feedback(raw_input=data.raw_input, generated_summary=summary)
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

