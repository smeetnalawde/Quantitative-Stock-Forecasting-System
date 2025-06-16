from sqlalchemy import Column, String, Float, Integer, Date, Text, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class SentimentData(Base):
    __tablename__ = 'sentiment_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ticker = Column(String(10))
    source = Column(String(50))
    api_vendor = Column(String(50))
    date = Column(Date)
    headline = Column(Text)
    sentiment_score = Column(Float)
    sentiment_label = Column(String(10))
    article_url = Column(Text)
    author = Column(String(255))
    platform_tags = Column(String(100))
    model_used = Column(String(50))
    confidence = Column(Float, default=None)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))
