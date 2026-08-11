from cli.delete_expense import choose_expense
from cli.menu import clear_screen
from cli.add_expense_menu import get_amount,get_description,choice_category
from database.database import Connection

def update_expense(expense):
    connection = Connection()
    cursor = connection.cursor()

    cursor.execute("""
    UPDATE costs
    SET amount = ?,
        category_id = ?,
        descriptions = ?
    WHERE id = ?
""", (
    expense[1],
    expense[2],
    expense[5],
    expense[0]
))

    connection.commit()
    connection.close()

def edit_expense():
    clear_screen()
    expense = choose_expense() 
    if expense is None:
         return 
    expense_id = expense[0]
    while (True):
        print("========== Edit Expense ==========") 
        print(f"ID: {expense[0]}") 
        print(f"Amount: {expense[1]}") 
        print(f"Category: {expense[3]}")
        print(f"Date: {expense[4]}") 
        print(f"Description: {expense[5] or ''}")
     
        print("\n1. Edit Amount") 
        print("2. Edit Category") 
        print("3. Edit Description") 
        print("0. Save & Exit")
        choice = input("\nSelect an option: ")

        match choice:
            case "1":
                amount=get_amount()
                expense[1]=amount
            case "2":
                category=choice_category()
                expense[2]=category
            case "3":
                description=get_description()
                expense[5]=description
            case "0":
                update_expense(expense)
                print("Expense updated successfully.")
                break
            case _: 
                print("Invalid option.")

        