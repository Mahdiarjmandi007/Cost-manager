import sqlite3
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
Database_path = BASE_DIR / "data" / "database.db"



DEFAULT_CATEGORIES = [
    "Food",
    "Transportation",
    "Shopping",
    "Entertainment",
    "Bills",
    "Health",
    "Education",
    "Rent",
    "Subscriptions",
    "Other",
]

def Connection ():
    Database_path.parent.mkdir(parents=True,exist_ok=True)

    return sqlite3.connect(Database_path)

def create_tables():
    connection=Connection()
    cursor=connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS categories(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
                   )
""")
    
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS costs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            amount REAL NOT NULL,
            category_id INTEGER NOT NULL,
            date TEXT NOT NULL,
            descriptions TEXT,
                   
                   FOREIGN KEY (category_id)
                    REFERENCES categories(id)               
                   )
""")
    connection.commit()
    connection.close()

def insert_default_categories():
    connection=Connection()
    cursor=connection.cursor()

    for category in DEFAULT_CATEGORIES:
        cursor.execute(
        "INSERT OR IGNORE INTO categories (name) VALUES (?)",
            (category,)
)    
    connection.commit()
    connection.close()
    

