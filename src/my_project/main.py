"""
Главный модуль приложения FastAPI — создание экземпляра приложения, подключение роутеров и
инициализация базы данных при старте.

Задачи этого файла:
- создать FastAPI app;
- подключить все маршрутизаторы (routers) приложения;
- при старте приложения обеспечить создание таблиц (Base.metadata.createall) и
  настроить нужные параметры СУБД.
"""

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

# Экземпляр FastAPI — единственная точка входа для ASGI-сервера (uvicorn, hypercorn и т.п.).
app = FastAPI()

# Подключаем роутеры — разделение по функциональности делает код чище.
app.include_router(router_for_users)
app.include_router(router_for_tasks)
app.include_router(user_router_for_service)
app.include_router(task_router_for_service)


@app.on_event("startup")
async def startup():
    """
    Событие старта приложения.

    Что делает:
    - создаёт все таблицы, описанные в Base.metadata (если таблицы отсутствуют);
    - выполняет дополнительную SQL-команду PRAGMA journalmode=WAL для улучшения поведения SQLite.

    :return: Функция не содержит return, поэтому по завершении возвращает None (неявно).
    """
    async with async_engine.begin() as conn:  # Открытие транзакционного контекста на уровне соединения асинхронного движка.
        await conn.run_sync(Base.metadata.create_all)  # Создание таблиц в случае, если они еще не созданы
        await conn.execute(
            text("PRAGMA journal_mode=WAL"))  # Режим журналирования WAL повышает конкуренцию записи/чтения.
