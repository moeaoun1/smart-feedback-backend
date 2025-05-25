from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    id = Column(Integer, primary_key=True, index=True)
    raw_input = Column(Text)
    generated_summary = Column(Text)
