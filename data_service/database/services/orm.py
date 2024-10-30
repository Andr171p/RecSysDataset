from sqlalchemy import select

from data_service.database.services.db import DatabaseSessionService
from data_service.database.models.student_inputs import StudentInputsModel
from data_service.database.models.student_outputs import StudentOutputsModel


class ORMService(DatabaseSessionService):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def create_tables(self) -> None:
        tables = [StudentInputsModel, StudentOutputsModel]
        async with self.connect() as connection:
            for table in tables:
                await connection.run_sync(table.metadata.drop_all)
                await connection.run_sync(table.metadata.create_all)


import asyncio

asyncio.run(ORMService().create_tables())