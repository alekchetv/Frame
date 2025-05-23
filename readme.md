# Описание
Это backend-сервис, разработанный с использованием FastAPI, предназначенный для оценки и обзора фильмов. Пользователи могут регистрироваться, добавлять оценки к фильмам и просматривать средние рейтинги по фильмам.

# Стек технологий:
- Python
- FastAPI
- SQLAlchemy + Alembic
- PostgreSQL
- JWT
- Pydantic
- Uvicorn 

# Реализованные возможности:
- Разработана система регистрации и аутентификации пользователей с использованием JWT токена
- Добавление/удаление/редактирование списка фильмов для каждого пользователя
- Реализован паттерн репозитория - для работы с БД написаны отдельные сущности и функции
- Реализован docker и docker compose для универсального развертывания проекта
- Реализован класс Exception ответа пользователю при возникновении ошибок

## Развертывание приложения:
Выполнить команду в корне проекта: `docker compose up`