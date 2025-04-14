import sqlite3
from passlib.hash import pbkdf2_sha256

# Create or connect to the SQLite database
conn = sqlite3.connect("users.db", check_same_thread=False)
cursor = conn.cursor()

# === Create Tables ===
def create_tables():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE,
            password TEXT,
            email TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            task_name TEXT,
            deadline TEXT,
            status TEXT DEFAULT 'Pending',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reminders (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            reminder_time TEXT
        )
    ''')

    conn.commit()

# === User Management ===
def add_user(username, password, email):
    hashed_pw = pbkdf2_sha256.hash(password)
    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)",
                   (username, hashed_pw, email))
    conn.commit()

def get_user(username):
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    return cursor.fetchone()

def authenticate_user(username, password):
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    if result:
        return pbkdf2_sha256.verify(password, result[0])
    return False

def get_user_email(username):
    cursor.execute("SELECT email FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    return result[0] if result else None

# === Task Management ===
def add_task(username, task_name, deadline):
    cursor.execute("INSERT INTO tasks (username, task_name, deadline) VALUES (?, ?, ?)",
                   (username, task_name, deadline))
    conn.commit()

def get_tasks(username):
    cursor.execute("SELECT * FROM tasks WHERE username=?", (username,))
    return cursor.fetchall()

def update_task_status(task_id, status):
    cursor.execute("UPDATE tasks SET status=? WHERE id=?", (status, task_id))
    conn.commit()

# === Reminders ===
def set_reminder(username, reminder_time):
    cursor.execute("INSERT INTO reminders (username, reminder_time) VALUES (?, ?)",
                   (username, reminder_time))
    conn.commit()

def get_reminder_time(username):
    cursor.execute("SELECT reminder_time FROM reminders WHERE username=?", (username,))
    result = cursor.fetchone()
    return result[0] if result else None

def get_tasks_by_username(username):
    cursor.execute("SELECT * FROM tasks WHERE username=?", (username,))
    return cursor.fetchall()

def get_tasks_for_user(username):
    cursor.execute("SELECT * FROM tasks WHERE username=?", (username,))
    return cursor.fetchall()
