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

def yearly():
    clear_screen()
    year=get_year()
    chosen_date = f"{year}-%-%"
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
    print(f"========== {year} ==========\n")
    if result[2] == 0:
        print("No expenses found.\n")
        return
    print(f"Total Expense: {result[0] or 0}")
    print(f"Average Expense: {result[1] or 0}")
    print(f"Number of Expenses: {result[2]}")
    while(True):
        choice= input("\nDo you want to see chart? (Y/N): ").lower()
        if choice=="y":
            plot_expense_chart(chosen_date,"yearly")
            return
        elif choice=="n":
            return
        else:
            print("Please enter a valid character.")

def by_category():
    clear_screen()
    print("========== Category Analysis ==========")
    print("1. Monthly")
    print("2. Yearly")
    print("3. All Time")
    print("0. Back")
    while(True):
        
        try:
            choice=int(input("Enter an option: "))
            if choice in [0,1,2,3]:
                break
            else:
                print("plese enter valid number ")
            
        except ValueError:
            print("please enter a number ")
    match choice:
        case 1:
                month=get_month()
                month = f"{month:02d}"
                year=get_year()
                chosen_date = f"{year}-{month}-%"
                query="""
                SELECT
                categories.name,
                SUM(costs.amount),
                COUNT(costs.id),
                AVG(costs.amount)
                FROM costs
                JOIN categories
                    ON costs.category_id = categories.id
                WHERE costs.date LIKE ?
                GROUP BY categories.id
                ORDER BY SUM(costs.amount) DESC;"""
                connection=Connection()
                cursor=connection.cursor()
                cursor.execute(query,(chosen_date,))
                result = cursor.fetchall()
                connection.close()
                if not result:
                    print("No expenses found for this period.")
                    input("Press Enter to continue...")
                    return
                print(f"========== {year}-{month} ==========\n")
                print("Category              Total      Count          Avg")
                print("-------------------------------------------------------")
                for category in result:
                    print(
                        f"{category[0]:<20}"
                        f"{category[1]:<15.2f}"
                        f"{category[2]:<10}"
                        f"{category[3]:<15.2f}"
                    )
        case 2:
                year=get_year()
                chosen_date = f"{year}-%-%"
                query="""
                SELECT
                categories.name,
                SUM(costs.amount),
                COUNT(costs.id),
                AVG(costs.amount)
                FROM costs
                JOIN categories
                    ON costs.category_id = categories.id
                WHERE costs.date LIKE ?
                GROUP BY categories.id
                ORDER BY SUM(costs.amount) DESC;"""
                connection=Connection()
                cursor=connection.cursor()
                cursor.execute(query,(chosen_date,))
                result = cursor.fetchall()
                connection.close()
                if not result:
                    print("No expenses found for this period.")
                    input("Press Enter to continue...")
                    return
                print(f"========== {year} ==========\n")
                print("Category              Total      Count          Avg")
                print("-------------------------------------------------------")
                for category in result:
                    print(
                        f"{category[0]:<20}"
                        f"{category[1]:<15.2f}"
                        f"{category[2]:<10}"
                        f"{category[3]:<15.2f}"
                    )
        case 3:
                query="""
                SELECT
                categories.name,
                SUM(costs.amount),
                COUNT(costs.id),
                AVG(costs.amount)
                FROM costs
                JOIN categories
                    ON costs.category_id = categories.id
                GROUP BY categories.id
                ORDER BY SUM(costs.amount) DESC;"""
                connection=Connection()
                cursor=connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                connection.close()
                if not result:
                    print("No expenses found for this period.")
                    input("Press Enter to continue...")
                    return
                print(f"========== All Time ==========\n")
                print("Category              Total      Count          Avg")
                print("-------------------------------------------------------")
                for category in result:
                    print(
                        f"{category[0]:<20}"
                        f"{category[1]:<15.2f}"
                        f"{category[2]:<10}"
                        f"{category[3]:<15.2f}"
                    )            
        case 0:
            return
