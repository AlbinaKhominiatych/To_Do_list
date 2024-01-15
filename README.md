# To-Do List API

This is a FastAPI web application for managing a To-Do List.

## Installation

1. Clone the repository:

     ```bash
     git clone https://github.com/your-username/your-repo.git
     ```

2. Go to the project directory:

     ```bash
     cd your-repo
     ```

3. Install dependencies:

     ```bash
     pip install -r requirements.txt
     ```

## Start the application

Use the command to start the Uvicorn server:

```bash
uvicorn main:app --reload
```

After launch, the application will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Using the API

### Get all users

```http
GET /users/
```

### Create a new user

```http
POST /users/
```

```json
{
     "username": "new_user",
     "email": "new_user@example.com"
}
```

### Get all user tasks

```http
GET /users/{user_id}/tasks/
```

### Create a new task for the user

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

And other endpoints...

## Contribution

If you have questions, bugs or suggestions, please open a [new issue](https://github.com/AlbinaKhominiatyche/To_Do_list/issues).

If you want to contribute a new feature or fix, please create a [new pull request](https://github.com/AlbinaKhominiatych/To_Do_list/pulls).

## License

This project is licensed under the MIT License - see [LICENSE](LICENSE) for details.
