# To-Do List API

Це FastAPI веб-додаток для управління списком завдань (To-Do List).

## Встановлення

1. Клонуйте репозиторій:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    ```

2. Перейдіть в каталог проєкту:

    ```bash
    cd your-repo
    ```

3. Встановіть залежності:

    ```bash
    pip install -r requirements.txt
    ```

## Запуск додатку

Використовуйте команду для запуску сервера Uvicorn:

```bash
uvicorn main:app --reload
```

Після запуску, додаток буде доступний за адресою [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Використання API

### Отримати всіх користувачів

```http
GET /users/
```

### Створити нового користувача

```http
POST /users/
```

```json
{
    "username": "new_user",
    "email": "new_user@example.com"
}
```

### Отримати всі завдання користувача

```http
GET /users/{user_id}/tasks/
```

### Створити нове завдання для користувача

```http
POST /users/{user_id}/tasks/
```

```json
{
    "title": "Complete task",
    "description": "Finish the task",
    "is_done": false
}
```

Та інші ендпойнти...

## Внесок

Якщо у вас є питання, помилки чи пропозиції, будь ласка, відкрийте [новий issue](https://github.com/AlbinaKhominiatyche/To_Do_list/issues).

Якщо ви хочете внести свій внесок у вигляді нової функції чи виправлення, будь ласка, створіть [новий pull request](https://github.com/AlbinaKhominiatych/To_Do_list/pulls).

## Ліцензія

Цей проєкт ліцензований під MIT License - деталі дивіться в файлі [LICENSE](LICENSE).
