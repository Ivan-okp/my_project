"""
Главный модуль приложения FastAPI — создание экземпляра приложения, подключение роутеров и
инициализация базы данных при старте.

Задачи этого файла:
- создать FastAPI app;
- подключить все маршрутизаторы (routers) приложения;
- при старте приложения обеспечить создание таблиц (Base.metadata.create_all) и
  настроить нужные параметры СУБД.
"""

from contextlib import asynccontextmanager
from fastapi import FastAPI
from sqlalchemy import text
from src.my_project.database_core.database import (
    Base,
    async_engine,
)
from src.my_project.routers import (
    router_for_users,
    router_for_tasks,
    user_router_for_service,
    task_router_for_service,
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """

    :param app: Экземпляр класса FastAPI.
    :return: Функция не содержит return, поэтому по завершении возвращает None (неявно).
    """
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        await conn.execute(text("PRAGMA journal_mode=WAL"))
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(router_for_users)
app.include_router(router_for_tasks)
app.include_router(user_router_for_service)
app.include_router(task_router_for_service)
