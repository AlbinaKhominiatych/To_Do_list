import requests

# Замініть URL на той, який ви використовуєте для вашого сервера FastAPI
base_url = "http://127.0.0.1:8000"

def add_task(user_id: int, title: str, description: str, is_done: bool):
    task_data = {
        "user_id": user_id,  # Додайте user_id до данних завдання
        "title": title,
        "description": description,
        "is_done": is_done
    }

    response = requests.post(f"{base_url}/users/{user_id}/tasks/", json=task_data)

    if response.status_code == 200:
        print("Task added successfully:")
        print(response.json())
    else:
        print("Failed to add task. Server response:")
        print(response.text)

if __name__ == "__main__":
    # Замініть параметри на ті, які ви хочете використовувати
    add_task(user_id=1, title="Complete project", description="Finish the FastAPI project", is_done=False)
