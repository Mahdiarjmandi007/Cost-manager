from analysis.reports import monthly,yearly,by_category
from cli.menu import clear_screen
def analysis_menu():
    clear_screen()
    print("========== Analysis ==========\n")
    print("1. Monthly Report")
    print("2. Yearly Report")
    print("3. Category Analysis")
    print("0. Back\n")
    while(True):
        
        try:
            choice=int(input("Enter an option: "))
            if choice in [0,1,2,3,4]:
                break
            else:
                print("plese enter valid number ")
            
        except ValueError:
            print("please enter a number ")

    match choice:
        case 1:
            monthly()
        case 2:
            yearly()
        case 3:
            by_category()
        case 0:
            return

