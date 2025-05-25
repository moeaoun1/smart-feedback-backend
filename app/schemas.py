from pydantic import BaseModel

class FeedbackRequest(BaseModel):
    raw_input: str

class FeedbackResponse(BaseModel):
    id: int
    raw_input: str
    generated_summary: str
