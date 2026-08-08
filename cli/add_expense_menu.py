import os
from datetime import date
from database.database import Connection

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

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")



def choice_category():
    print("===SELECT CATEGORY===")
    for i in range(len(DEFAULT_CATEGORIES)):
        print(f"{i+1}. {DEFAULT_CATEGORIES[i]}")
    while(True):
        try:
            choice=int(input("Select Category:"))
            if choice >=1 and choice<=10:
                break
            print("Please enter a number between 1 and 10.")
        except ValueError:
            print("Please enter a valid number.")
    return choice
def get_amount():
    print("+"*20)
    while(True):
        try:
            amount=int(input("Enter Amount: "))
            if amount > 0:
                return amount
            print("Amount must be greater than 0.")
        except ValueError:
            print("Please enter a valid amount")

    
def get_description():
    print("+"*20)
    return input("write description: ") 


def add_expense_menu():
    clear_screen()
    category_id=choice_category()
    amount=get_amount()
    description=get_description()
    today = date.today().isoformat()


    connection = Connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO costs (amount, category_id, date, descriptions)
        VALUES (?, ?, ?, ?)
    """, (amount, category_id, today, description))

    connection.commit()
    connection.close()