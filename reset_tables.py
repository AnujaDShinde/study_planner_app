# reset_tables.py
import sqlite3

def reset_users_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Drop and recreate the users table
    cursor.execute("DROP TABLE IF EXISTS users")
    cursor.execute("""
        CREATE TABLE users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()
    print("✅ users table reset successfully!")

def reset_tasks_table():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # Drop and recreate the tasks table with status column
    cursor.execute("DROP TABLE IF EXISTS tasks")
    cursor.execute("""
        CREATE TABLE tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            task TEXT NOT NULL,
            due_date TEXT NOT NULL,
            status TEXT DEFAULT 'Pending'
        )
    """)

    conn.commit()
    conn.close()
    print("✅ tasks table reset successfully!")

def reset_all_tables():
    reset_users_table()
    reset_tasks_table()

if __name__ == "__main__":
    reset_all_tables()
