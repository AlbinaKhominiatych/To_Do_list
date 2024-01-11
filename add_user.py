import requests

url = "http://127.0.0.1:8000/users/"

# Дані нового користувача
new_user = {
    "username": "john_doe",
    "email": "john.doe@example.com",
}

# Виклик POST-запиту для додавання нового користувача
response = requests.post(url, json=new_user)

# Виведення результату
print(response.status_code)
print(response.json())
