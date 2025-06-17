from sqlalchemy import Column, String, Float, Date, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime, timezone

Base = declarative_base()

class MacroData(Base):
    __tablename__ = 'macro_data'

    date = Column(Date, primary_key=True)
    indicator_name = Column(String(100), primary_key=True)
    value = Column(Float)
    source = Column(String(100))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
