from fastapi import FastAPI, status

from src.api.question import create_question
from src.schema import QuestionSchema


def add_routes(app: FastAPI) -> None:
    app.add_api_route(
        path='/api/questions',
        endpoint=create_question,
        status_code=status.HTTP_201_CREATED,
        response_model=QuestionSchema,
        methods=['post'],
    )
