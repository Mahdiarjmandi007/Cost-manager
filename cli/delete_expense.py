from database.database import Connection

from cli.menu import clear_screen

def choose_expense():
    connection = Connection()
    cursor = connection.cursor()
    print("\n========== Select Expense ==========") 
    print("1. Last 10 expenses") 
    print("2. Last 15 expenses") 
    print("3. All expenses") 
    print("0. Back")
    while (True):
        try:
            choice = int(input("\nSelect an option: "))
            if choice in [0,1,2,3]:
                break
            print("Please select a valid option.")
        except ValueError: 
            print("Please enter a valid number.")
    if choice ==0:
        connection.close()
        return None
    if choice == 1:
        Limit=10
    if choice == 2:
        Limit=15
    if choice == 3:
        Limit=None
    query = """
        SELECT
        costs.id,
        costs.amount,
        costs.category_id,
        categories.name,
        costs.date,
        costs.descriptions
        FROM costs
        JOIN categories
        ON costs.category_id = categories.id
        ORDER BY costs.id DESC
        """
    if Limit is not None:
        query += " LIMIT ?"
        cursor.execute(query, (Limit,))
    else:
        cursor.execute(query)
    expenses = cursor.fetchall()
    if not expenses: 
        connection.close() 
        print("No expenses found.") 
        return None
    print("\nID    Amount       Category          Date          Description")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense[0]:<6}"
            f"{expense[1]:<13}"
            f"{expense[3]:<18}"
            f"{expense[4]:<14}"
            f"{expense[5] or ''}"
        )
    while True:
        try: 
            expense_id = int(input("\nEnter Expense ID: ")) 
            for expense in expenses: 
                if expense[0] == expense_id: 
                    connection.close() 
                    return list(expense) 
            print("Please enter an ID from the list.") 
        except ValueError:
            print("Please enter a valid ID.")

def delete_expense():
    clear_screen()
    expense = choose_expense() 
    if expense is None: 
        return
    expense_id = expense[0] 
    print("\nSelected expense:") 
    print(f"ID: {expense[0]}") 
    print(f"Amount: {expense[1]}") 
    print(f"Category: {expense[3]}") 
    print(f"Date: {expense[4]}") 
    print(f"Description: {expense[5] or ''}")
    while True: 
        confirm = input("\nAre you sure you want to delete it? (y/n): ").lower() 
        if confirm == "y": 
            break 
        if confirm == "n": 
            print("Deletion cancelled.") 
            return 
        print("Please enter y or n.")
    connection = Connection() 
    cursor = connection.cursor() 
    cursor.execute(
         "DELETE FROM costs WHERE id = ?", (expense_id,) 
         )
    connection.commit() 
    connection.close()
    print("Expense deleted successfully.")

