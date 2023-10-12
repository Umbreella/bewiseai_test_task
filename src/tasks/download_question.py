from httpx import AsyncClient, Response

from src.db import database
from src.manager import QuestionManager
from src.schema import QuestionSchema


async def download_question(
    questions_num: int,
) -> None:
    async with database.session() as session, session.begin():
        while questions_num != 0:
            url: str = f'https://jservice.io/api/random?count={questions_num}'

            response: Response = await AsyncClient().get(url=url)

            for question_data in response.json():
                data: QuestionSchema = QuestionSchema.model_validate(
                    question_data,
                )

                question = await QuestionManager.create(data, session)

                if question:
                    questions_num -= 1
