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
        print("3. Analysis")
        print("4. Exit")
        print("\n")

        choice = int(input("Enter your choice(1/2/3) : "))

        if choice == 1:
            add_logs()

        elif choice == 2:
            view_history()

        elif choice == 3:
            analysis()

        elif choice == 4:
            break

        else:
            print("Invalid Choice. Please Try again.")
        
        print("\n")

def analysis():
    try:
        with open("Code_Tracker.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present

            total_lines = 0
            line_counts = []  # Store lines of code for calculation
            data_list = []
            for row in reader:
                date_object = datetime.datetime.strptime(row[0], "%d-%m-%Y")  # Convert date string to datetime
                lines = int(row[1])  # Convert lines to integer
                line_counts.append(lines)  # Store in list

                data_list.append((date_object,lines))
            best_day = max(data_list,key=lambda x : x[1])

            total_lines = sum(line_counts)  # Calculate total lines
            average_lines = total_lines / len(line_counts) if line_counts else 0  # Avoid division by zero

            print(f"Total Lines of Code Written: {total_lines}")
            print(f"Average Lines Per Day: {average_lines:.2f}")
            print(f"Best Coding Day: {best_day[0].strftime('%d-%m-%Y')}")
            print(f"Lines of Code Written on Best Day: {best_day[1]}")

    except FileNotFoundError:
        print("Error. No Coding History Found.\n")


#Call main function

show_menu()


