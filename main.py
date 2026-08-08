from database.database import create_tables, insert_default_categories,DEFAULT_CATEGORIES
from cli.menu import *

def create_database():
    
    create_tables()
    insert_default_categories()

    print("Database initialized successfully.")

def main ():
    create_database()
    while True:
        choice = show_main_menu()
        match choice:
            case "1":
                print("Add Expense")

            case "2":
                print("View Expenses")

            case "3":
                print("Edit Expense")

            case "4":
                print("Delete Expense")

            case "5":
                print("Reports")

            case "6":
                print("Categories")

            case "0":
                print("Goodbye!")
                break

            case _:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    create_database()