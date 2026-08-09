from database.database import create_tables, insert_default_categories,DEFAULT_CATEGORIES
from cli.menu import show_main_menu
from cli.add_expense_menu import add_expense_menu
from cli.delete_expense import delete_expense
from cli.edit_expense import edit_expense
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
                add_expense_menu()

            case "2":
                print('m')

            case "3":
                edit_expense()

            case "4":
                delete_expense()

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
    main()
    