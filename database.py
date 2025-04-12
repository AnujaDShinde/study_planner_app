import sqlite3
from passlib.hash import pbkdf2_sha256

# Create the users table
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

# Create the tasks table
def create_task_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            task TEXT NOT NULL,
            due_date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Create both tables
def create_tables():
    create_users_table()
    create_task_table()

# Add a new user
def add_user(username, password, role):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    
    # Hash the password before saving
    hashed_password = pbkdf2_sha256.hash(password)
    
    cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                   (username, hashed_password, role))
    conn.commit()
    conn.close()

# Authenticate user credentials
def authenticate_user(username, password):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result:
        stored_password = result[0]
        # Verify hashed password
        return pbkdf2_sha256.verify(password, stored_password)
    return False

# Get full user row by username
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()
    return user

# Add a task for a user
def add_task(username, task, due_date):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (username, task, due_date) VALUES (?, ?, ?)",
                   (username, task, due_date))
    conn.commit()
    conn.close()

# Retrieve tasks for a user
def get_tasks_for_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("SELECT task, due_date FROM tasks WHERE username = ?", (username,))
    tasks = cursor.fetchall()
    conn.close()
    return tasks


