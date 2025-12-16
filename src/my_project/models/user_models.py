"""
Модуль модели пользователя (UserModel) для SQLAlchemy.

Содержит декларативную модель UserModel, которая описывает таблицу пользователей
в базе данных и связанное с ней ORM-отношение к задачам пользователя.
"""

from sqlalchemy import (
    Column,
    Integer,
    String
)
from sqlalchemy.orm import relationship
from src.my_project.database_core.database import Base


class UserModel(Base):
    """
    Модель пользователя.

    Атрибуты:
    - id: первичный ключ (целое число).
    - name: имя пользователя.
    - email: адрес электронной почты.
    - password: пароль.
    - tasks: ORM-отношение к задачам пользователя (список TaskModel), двунаправленное
      через backpopulates="author" в TaskModel.
    """
    __tablename__ = "users"   # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Уникальный идентификатор пользователя
    name = Column(String, unique=True)  # Имя пользователя
    email = Column(String, unique=True)  # Адрес электронной почты пользователя
    password = Column(String)  # Пароль пользователя
    tasks = relationship("TaskModel", back_populates="author")  # Отношение к модели задач (TaskModel).
