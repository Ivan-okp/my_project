"""
Модуль модели задач (TaskModel) для SQLAlchemy.

Содержит декларативную модель TaskModel, описывающую таблицу задач в базе данных.
Модель хранит минимальный набор полей: идентификатор, заголовок, тело,
статус и связь с пользователем-автором.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship
from src.my_project.database_core.database import Base


# Декларативная модель, представляющая таблицу "tasks"
class TaskModel(Base):
    """
    Модель задачи.

    Атрибуты:
    - id: первичный ключ (целое число).
    - title: заголовок задачи (строка).
    - body: подробное описание задачи (строка).
    - status: строковое поле для статуса задачи.
    - user: целочисленное поле, содержащее внешний ключ на таблицу users (users.id).
    - author: ORM-отношение (relationship) к модели UserModel; связывает задачу с её автором.
      Свойство back_populates должно соответствовать атрибуту в UserModel, который содержит
      список задач (например, tasks).
    """
    __tablename__ = "tasks"  # Имя таблицы в базе данных

    id = Column(Integer, primary_key=True)  # Уникальный идентификатор задачи
    title = Column(String)  # Название задачи
    body = Column(String)  # Описание содержания задачи
    status = Column(String)  # Статус задачи
    user = Column(Integer, ForeignKey("users.id"))  # ID пользователя, создавшего задачу
    author = relationship("UserModel", back_populates="tasks")  # Отношение к модели пользователя (UserModel)
