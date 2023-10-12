from fastapi import BackgroundTasks, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.responses import JSONResponse

from src.db import get_db
from src.models import Question
from src.schema import QuestionCreateSchema, QuestionSchema
from src.tasks import download_question


async def create_question(
    data: QuestionCreateSchema,
    background_tasks: BackgroundTasks,
    session: AsyncSession = Depends(get_db),
) -> QuestionSchema | JSONResponse:

    background_tasks.add_task(download_question, data.questions_num)

    question: Question | None = (await session.execute(
        select(Question).order_by(Question.saved_at.desc()),
    )).scalars().first()

    if not question:
        return JSONResponse(content={})

    return QuestionSchema.model_validate(question)
