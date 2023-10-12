from datetime import datetime

from pydantic import BaseModel, ConfigDict


class QuestionCreateSchema(BaseModel):
    questions_num: int


class QuestionSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    question: str
    answer: str
    created_at: datetime
