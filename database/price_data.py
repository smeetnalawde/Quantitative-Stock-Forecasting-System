from sqlalchemy import Column, String, Float, BigInteger, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PriceData(Base):
    __tablename__ = 'price_data'

    ticker = Column(String(10), primary_key=True)
    date = Column(Date, primary_key=True)
    interval = Column(String(10), primary_key=True)
    source_api = Column(String(50), primary_key=True)

    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    adjusted_close = Column(Float)
    volume = Column(BigInteger)
    currency = Column(String(10))
    data_type = Column(String(10))
    created_at = Column(DateTime, default=datetime.utcnow)
