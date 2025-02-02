import datetime
import csv


def add_logs():

    current_date = datetime.datetime.now().strftime("%d-%m-%Y")
    

    no_of_lines = int(input("Enter the number of lines you did today(Approximate) : "))
    

    with open("Code_Tracker.csv","a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([current_date,no_of_lines])

    print("CSV file written successfully")
    print("\n")

def view_history():

    try:
        with open("Code_Tracker.csv","r") as file:
            reader = csv.reader(file)
            for i in reader:
                print(i)
            print("\n")
    except FileNotFoundError:
        print("Error. No Coding History Found.")
        print("\n")

def show_menu():
    
    while True:
        print("Hello, Welcome to Coding Tracker.")
        print("What would you like to do : ")
        print("1. Enter Logs for Today.")
        print("2. View Logs History.")
        print("3. Exit.")
        print("\n")

        choice = int(input("Enter your choice(1/2/3) : "))

        if choice == 1:
            add_logs()

        elif choice == 2:
            view_history()

        elif choice == 3:
            break;

        else:
            print("Invalid Choice. Please Try again.")
        
        print("\n")

#Call main function

show_menu()


