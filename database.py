import sqlite3

def create_connection():
    return sqlite3.connect("reviews.db")

def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        age INTEGER
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        email TEXT,
        age INTEGER,
        review TEXT,
        prediction TEXT,
        probability REAL
    )
    """)

    conn.commit()
    conn.close()


def save_user(username, email, age):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO users (username, email, age)
    VALUES (?, ?, ?)
    """, (username, email, age))

    conn.commit()
    conn.close()


def save_review(username, email, age, review, prediction, prob):
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reviews (username, email, age, review, prediction, probability)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (username, email, age, review, prediction, prob))

    conn.commit()
    conn.close()


def get_all_reviews():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT username, email, age, review, prediction, probability
    FROM reviews
    """)

    data = cursor.fetchall()
    conn.close()

    return data