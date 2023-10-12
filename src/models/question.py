from datetime import datetime

from sqlalchemy import BigInteger, Column, DateTime, Text

from src.db import BASE


class Question(BASE):
    __tablename__ = 'questions'

    id = Column(BigInteger, primary_key=True)
    question = Column(Text, nullable=False)
    answer = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False)

    saved_at = Column(DateTime, default=datetime.utcnow)
