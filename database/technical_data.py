from sqlalchemy import Column, String, Float, BigInteger, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class TechnicalFeatures(Base):
    __tablename__ = "technical_features"

    ticker = Column(String, primary_key=True)
    date = Column(DateTime, primary_key=True)
    close = Column(Float)
    volume = Column(BigInteger)
    return_1d = Column(Float)
    sma_5 = Column(Float)
    sma_20 = Column(Float)
    ema_10 = Column(Float)
    rsi_14 = Column(Float)
    macd = Column(Float)
