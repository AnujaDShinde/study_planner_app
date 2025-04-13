import sqlite3
from passlib.hash import pbkdf2_sha256

# Create users table
def create_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Create tasks table with status
def create_task_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            task TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)
    conn.commit()
    conn.close()

def create_tables():
    create_users_table()
    create_task_table()


def add_user(username, password, role):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Check if user already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    existing_user = cursor.fetchone()

    if existing_user:
        conn.close()
        raise ValueError("Username already exists. Please choose a different one.")

    hashed_password = pbkdf2_sha256.hash(password)
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   (username, hashed_password, role))
    conn.commit()
    conn.close()


def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return pbkdf2_sha256.verify(password, result[0])
    return False

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

def add_task(username, task, due_date):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (username, task, due_date) VALUES (?, ?, ?)",
                   (username, task, due_date))
    conn.commit()
    conn.close()

def get_tasks_for_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, task, due_date, status FROM tasks WHERE username = ?", (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks

def update_task_status(task_id, new_status):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (new_status, task_id))
    conn.commit()
    conn.close()

# Add this function to your database.py file

# Retrieve tasks for a specific user, including their task status
def get_tasks_by_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks WHERE username = ?", (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks
