import sqlite3

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price TEXT NOT NULL,
        description TEXT NOT NULL,
        teacher_info TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def insert_row_employee(name, price, description, teacher_info):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO courses (name, price, description, teacher_info)
    VALUES (?, ?, ?, ?)
    """, (name, price, description, teacher_info))
    conn.commit()
    conn.close()

def fetch_all_courses():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT name, price, description, teacher_info FROM courses")
    courses = cursor.fetchall()
    conn.close()
    return courses
