import os
from datetime import date
from database.database import Connection
from cli.menu import clear_screen,get_categories



def choice_category():
    DEFAULT_CATEGORIES=get_categories()
    clear_screen()
    print("===SELECT CATEGORY===")
    for i in range(len(DEFAULT_CATEGORIES)):
        print(f"{DEFAULT_CATEGORIES[i][0]}. {DEFAULT_CATEGORIES[i][1]}")
    while(True):
        try:
            choice=int(input("Select Category:"))
            if choice >=1 and choice<len(DEFAULT_CATEGORIES):
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