"""
Набор тест-кейсов для роутера задач (task router).

Этот модуль содержит параметризованные данные (test cases), которые используются в
юнит-/интеграционных тестах для проверки эндпоинтов, связанных с задачами.
Каждый элемент в списках — кортеж, описывающий входные данные и ожидаемое поведение
API при определённом сценарии.
"""

test_cases_task_router_for_get_task = [
    (
        1,
        200,
        {"title": f"testtask_1", "body": f"testbody_1_for_testtask1", "status": "New", "user": 1},
    ),
    (
        4,  # id выходит из диапазона
        404,
        None,
    ),
    (
        True,  # неверный формат id
        422,
        None,
    ),
    (
        None,  # id отсутствует
        422,
        None,
    ),
]

test_cases_task_router_for_add_task = [
    (
        {"title": "task_for_test", "body": "body for test task", "status": "New", "user": 1},
        200,
        {"title": "task_for_test", "body": "body for test task", "status": "New", "user": 1, "id": 1},
    ),
    (
        {"body": "body for test task", "status": "New", "user": 1},  # нет названия
        422,
        None,
    ),
    (
        {"title": "task_for_test", "status": "New", "user": 1},  # нет тела задачи
        422,
        None,
    ),
    (
        {"title": "task_for_test", "body": "body for test task", "user": 1},  # нет статуса
        422,
        None,
    ),
    (
        {"title": "task_for_test", "body": "body for test task", "status": "New"},  # нет пользователя
        422,
        None,
    ),
    (
        {"title": 12345, "body": "body for test task", "status": "New", "user": 1},  # неверный формат названия
        422,
        None,
    ),
    (
        {"title": "task_for_test", "body": 12345, "status": "New", "user": 1},  # неверный формат описания задачи
        422,
        None,
    ),
    (
        {"title": "task_for_test", "body": "body for test task", "status": "Old", "user": 1},
        # неверный формат статуса задачи
        422,
        None,
    ),
    (
        {"title": "task_for_test", "body": "body for test task", "status": "New", "user": "user"},
        # неверный формат пользователя
        422,
        None,
    ),
]

test_cases_task_router_for_update_task = [
    (
        0,
        1,
        {"title": "test add task", "body": "test body for test add", "status": "New"},
        200,
        {"id": 1, "title": "test add task", "body": "test body for test add", "status": "New", "user": 1},
    ),
    (
        0,
        None,  # отсутствует id
        {"title": "test add task", "body": "test body for test add", "status": "New"},
        422,
        None,
    ),
    (
        0,
        11,  # id выходит из диапазона
        {"title": "test add task", "body": "test body for test add", "status": "New"},
        404,
        None,
    ),
    (
        0,
        False,  # id имеет неверный формат
        {"title": "test add task", "body": "test body for test add", "status": "New"},
        422,
        None,
    ),
    (
        0,
        1,
        {"body": "test body for test add", "status": "New"},  # отсутствует название задачи
        422,
        None,
    ),
    (
        0,
        1,
        {"title": "test add task", "status": "New"},  # отсутствует описание задачи
        422,
        None,
    ),
    (
        0,
        1,
        {"title": "test add task", "body": "test body for test add"},  # отсутствует статус
        422,
        None,
    ),
]

test_cases_task_router_for_delete_task = [
    (
        0,
        1,
        200,
        {"message": "Task with ID 1 deleted successfully"},
    ),
    (
        0,
        None,  # id отсутствует
        422,
        None,
    ),
    (
        0,
        4,  # id выходит из диапазона
        404,
        None,
    ),
    (
        0,
        False,  # id имеет неверный формат
        422,
        None,
    ),
]
