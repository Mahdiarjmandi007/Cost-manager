from analysis.reports import monthly
from cli.menu import clear_screen
def analysis_menu():
    clear_screen()
    print("========== Analysis ==========\n")
    print("1. Monthly Report")
    print("2. Yearly Report")
    print("3. Category Analysis")
    print("4. Overall Statistics")
    print("0. Back\n")
    while(True):
        choice=int(input("Enter an option: "))
        try:
            if choice in [0,1,2,3,4]:
                break
            else:
                print("plese enter valid number ")
            
        except ValueError:
            print("please enter a number ")
    match choice:
        case 1:
            monthly()
        case 0:
            return

