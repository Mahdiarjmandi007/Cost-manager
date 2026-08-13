from database.database import Connection
from analysis.show_charts import plot_expense_chart
from cli.menu import clear_screen

def get_month():
    while True:
        try:
            month = int(input("Enter month (1-12): "))

            if 1 <= month <= 12:
                return month

            print("Month must be between 1 and 12.")

        except ValueError:
            print("Please enter a valid number.")

def get_year():
    while True:
        try:
            year = int(input("Enter year: "))

            if year >= 2000:
                return year

            print("Please enter a valid year.")

        except ValueError:
            print("Please enter a valid number.")


def monthly():
    month=get_month()
    month = f"{month:02d}"
    year=get_year()
    chosen_date = f"{year}-{month}-%"
    connection=Connection()
    cursor=connection.cursor()
    cursor.execute("""
                SELECT 
                    SUM(amount),
                    AVG(amount),
                    COUNT(*)
                FROM costs
                WHERE date LIKE ?
                  """,(chosen_date,))
    result = cursor.fetchone()
    connection.close()
    clear_screen()
    print(f"========== {year}-{month} ==========\n")
    if result[2] == 0:
        print("No expenses found.\n")
        return
    print(f"Total Expense: {result[0] or 0}")
    print(f"Average Expense: {result[1] or 0}")
    print(f"Number of Expenses: {result[2]}")
    while(True):
        choice= input("\nDo you want to see chart? (Y/N): ").lower()
        if choice=="y":
            plot_expense_chart(chosen_date,"monthly")
            return
        elif choice=="n":
            return
        else:
            print("Please enter a valid character.")



