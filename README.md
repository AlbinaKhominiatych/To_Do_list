# To-Do List App

Це веб-додаток "Список справ", створений за допомогою FastAPI та SQLAlchemy.

## Встановлення

1. Склонуйте репозиторій:

    ```bash
    git clone https://github.com/yourusername/to-do-list-app.git
    ```

2. Встановіть залежності:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск

Запустіть сервер FastAPI:

```bash
uvicorn main:app --reload
```

Відкрийте ваш браузер та перейдіть за адресою [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Використання

### Додавання нового користувача

Використовуйте HTTP POST запит:

```bash
http POST http://127.0.0.1:8000/users/ title="John Doe" email="john@example.com"
```

### Додавання нового завдання користувачу

Використовуйте HTTP POST запит:

```bash
http POST http://127.0.0.1:8000/users/1/tasks/ title="Complete task" description="Finish the task" is_done=false
```

## Документація API

Додаткову інформацію про доступні ендпоінти можна знайти в [документації API](http://127.0.0.1:8000/docs).

## Структура проекту

- `main.py`: Головний файл з FastAPI додатком та логікою маршрутів.
- `models.py`: Моделі бази даних SQLAlchemy.
- `schemas.py`: Схеми для валідації даних в запросах та відповідях.
- `add_task.py`: Приклад скрипта для додавання завдань через HTTP запит.

## Внесок

Якщо у вас є пропозиції чи покращення, будь ласка, відкривайте нові [issues](https://github.com/AlbinaKhominiatych/to-do-list-app/issues) чи присилайте [pull requests](https://github.com/AlbinaKhominiatych/to-do-list-app/pulls).

## Ліцензія

Цей проект розповсюджується під ліцензією [MIT](LICENSE).
