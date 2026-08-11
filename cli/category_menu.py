from cli.menu import get_categories,clear_screen
from database.database import Connection
import sqlite3
def category_menu():
    while(True):
        print("========== Category Menu ==========\n")
        print("1. Add Category")
        print("2. View Categories")
        print("0. Back")
        choose=input("choose an option")
        match choose:
            case "1":
                input_category=input("Enter Category Name:").strip()
                if not input_category: 
                    print("Category name cannot be empty.") 
                    input("Press Enter to continue") 
                    continue
                try:
                    connection = Connection()
                    cursor = connection.cursor()

                    cursor.execute("""
                    INSERT INTO categories (name)
                    VALUES (?)
                    """, (input_category,))

                    connection.commit()
                    connection.close()

                    print("Category added successfully.")

                except sqlite3.IntegrityError:
                    print("This category already exists.")

                except sqlite3.Error as error:
                    print(f"Database error: {error}")

                input("Press Enter to continue")
            case "2":
                categories=get_categories()
                print("========== Categories ==========")
                for category in categories:
                    print(f"{category[0]}. {category[1]}")
                input("Press Enter to return")
            case "0":
                return
            case _:
                clear_screen()
                "\t\tPleas Enter The Invalid Number"
