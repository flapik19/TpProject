import os
import json

DB_FILE = "./user_data.json"

def load_users():
    if not os.path.exists(DB_FILE):  # Если файл не существует
        with open(DB_FILE, "w") as db_file:
            db_file.write("[]")  # Создаем файл с пустым списком JSON
    try:
        with open(DB_FILE, "r") as db_file:
            return json.load(db_file)  # Просто возвращаем список
    except (json.JSONDecodeError, ValueError):  # Если файл поврежден или пуст
        with open(DB_FILE, "w") as db_file:
            db_file.write("[]")  # Перезаписываем файл пустым списком
        return []

def save_users(users):
    with open(DB_FILE, "w") as db_file:
        json.dump(users, db_file, indent=4)  # Сохраняем список

def addUser(username, password, role):
    users = load_users()  # Получаем список пользователей
    # Проверяем, существует ли пользователь с таким именем
    if any(user["username"] == username for user in users):
        return False  # Пользователь уже существует

    # Добавляем нового пользователя
    new_user = {"username": username, "password": password, "role": role}
    users.append(new_user)

    save_users(users)  # Сохраняем обновленный список
    return True
