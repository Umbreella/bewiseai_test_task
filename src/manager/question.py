from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.models import Question
from src.schema import QuestionSchema


class QuestionManager:
    @classmethod
    async def create(
        cls,
        data: QuestionSchema,
        session: AsyncSession,
    ) -> Question | None:
        query = insert(Question).values(
            **data.model_dump(),
        ).on_conflict_do_nothing().returning(Question)

        return (await session.execute(query)).scalar_one_or_none()
