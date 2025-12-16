"""
Набор параметризованных тест-кейсов для роутера пользователей (user router).

Этот модуль содержит данные (test cases), используемые в юнит-/интеграционных тестах для проверки
эндпойнтов, связанных с пользователями.
"""

test_cases_user_router_for_get_user = [
    (
        1,
        200,
        {"name": "testuser_1", "email": "testuser_1@example.com", "password": "1234567891"},
    ),
    (
        4, # id выходит из диапазона
        404,
        None,
    ),
    (
        True, # неверный формат id
        422,
        None,
    ),
    (
        None, # id отсутствует
        422,
        None,
    ),
]

test_cases_user_router_for_add_user = [
    (
        {"name": "test user", "email": "test@mail.com", "password": "123456789"},
        200,
        {"name": "test user", "email": "test@mail.com", "password": "123456789", "id": 1},
    ),
    (
        {"email": "test@mail.com", "password": "123456789"},  # Нет имени
        422,
        None,
    ),
    (
        {"name": "test user", "password": "123456789"},  # Нет email
        422,
        None,
    ),
    (
        {"name": "test user", "email": "test@mail.com"},  # Нет пароля
        422,
        None,
    ),
    (
        {"name": 12345, "email": "test@mail.com", "password": "123456789"}, # Неверный формат имени
        422,
        None,
    ),
    (
        {"name": "test user", "email": 12345, "password": "123456789"}, # Неверный формат email
        422,
        None,
    ),
    (
        {"name": "test user", "email": "test@mail.com", "password": 12345}, # Неверный формат пароля
        422,
        None,
    ),
]

test_cases_user_router_for_update_user = [
    (
        1,
        {"name": "test user update", "email": "test@update.com", "password": "987654321"},
        200,
        {"name": "test user update", "email": "test@update.com", "password": "987654321", "id": 1},
    ),
    (
        None, # id отсутствует
        {"name": "test user update", "email": "test@update.com", "password": "987654321"},
        422,
        None,
    ),
    (
        11, # id выходит из диапазона
        {"name": "test user update", "email": "test@update.com", "password": "987654321"},
        404,
        None,
    ),
    (
        False, # id имеет неверный формат
        {"name": "test user update", "email": "test@update.com", "password": "987654321"},
        422,
        None,
    ),
    (
        1,
        {"email": "test@update.com", "password": "987654321"}, # Отсутствует имя пользователя
        422,
        None,
    ),
    (
        1,
        {"name": "test user update", "password": "987654321"}, # Отсутствует email
        422,
        None,
    ),
    (
        1,
        {"name": "test user update", "email": "test@update.com"}, # Отсутствует пароль
        422,
        None,
    ),
    (
        1,
        {"name": 12345, "email": "test@update.com", "password": "987654321"}, # Неверный формат имени
        422,
        None,
    ),
    (
        1,
        {"name": "test user update", "email": 12345, "password": "987654321"}, # Неверный формат email
        422,
        None,
    ),
    (
        1,
        {"name": "test user update", "email": "test@update.com", "password": 12345}, # Неверный формат пароля
        422,
        None,
    ),
]

test_cases_user_router_for_delete_user = [
    (
        1,
        200,
        {"message": "User with ID 1 deleted successfully"},
    ),
    (
        4, # id выходит из диапазона
        404,
        None,
    ),
    (
        True, # неверный формат id
        422,
        None,
    ),
    (
        None, # id отсутствует
        422,
        None,
    ),
]