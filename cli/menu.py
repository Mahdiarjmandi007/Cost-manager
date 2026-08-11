import os
from database.database import Connection

def get_categories():
    connection = Connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM categories
        ORDER BY id
    """)

    categories = cursor.fetchall()

    connection.close()

    return categories


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_main_menu():
    clear_screen()
    print("\n"+"="*20)
    print("Cost Manager")
    print("="*20)

    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Edit Expense")
    print("4. Delete Expense")
    print("5. Reports")
    print("6. Categories")
    print("0. Exit")

    return input("Select an option:")


    
    
    
    
    
    