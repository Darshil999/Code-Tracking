import datetime
import csv

class Code:
    def add_logs():
        """Add today's coding log and update streaks."""

        current_date = datetime.datetime.now().strftime("%d-%m-%Y")
        no_of_lines = int(input("Enter the number of lines you did today (Approximate): "))

        try:
            with open("Code_Tracker.csv", "r") as file:
                reader = list(csv.reader(file))
                last_entry = reader[-1] if len(reader) > 1 else None
        except FileNotFoundError:
            last_entry = None

        if last_entry:
            last_date_str, _, last_streak = last_entry
            last_date = datetime.datetime.strptime(last_date_str, "%d-%m-%Y")
            streak = int(last_streak)

            if (datetime.datetime.now() - last_date).days == 1:
                streak += 1  # Continue streak
            else:
                streak = 1  # Reset streak
        else:
            streak = 1  # First entry

        with open("Code_Tracker.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([current_date, no_of_lines, streak])

        print(f"Log added successfully! Your current streak: {streak} days.\n")


    def view_history():
        """Display the coding log history."""
        try:
            with open("Code_Tracker.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
                print("\n")
        except FileNotFoundError:
            print("Error. No Coding History Found.\n")


    def analysis():
        """Analyze coding performance and streaks."""
        try:
            with open("Code_Tracker.csv", "r") as file:
                reader = csv.reader(file)
                next(reader)  # Skip header if present

                total_lines = 0
                line_counts = []
                streaks = []
                data_list = []

                for row in reader:
                    date_object = datetime.datetime.strptime(row[0], "%d-%m-%Y")
                    lines = int(row[1])
                    streak = int(row[2])

                    line_counts.append(lines)
                    streaks.append(streak)
                    data_list.append((date_object, lines, streak))

                total_lines = sum(line_counts)
                average_lines = total_lines / len(line_counts) if line_counts else 0
                best_day = max(data_list, key=lambda x: x[1]) if data_list else None
                highest_streak = max(streaks) if streaks else 0

                print(f"Total Lines of Code Written: {total_lines}")
                print(f"Average Lines Per Day: {average_lines:.2f}")
                if best_day:
                    print(f"Best Coding Day: {best_day[0].strftime('%d-%m-%Y')}")
                    print(f"Lines of Code on Best Day: {best_day[1]}")
                print(f"🔥 Highest Streak: {highest_streak} days")
                print(f"🔥 Current Streak: {streaks[-1] if streaks else 0} days\n")

        except FileNotFoundError:
            print("Error. No Coding History Found.\n")


    # def show_menu():
    #     """Display the main menu and handle user choices."""
    #     while True:
    #         print("📌 Welcome to Coding Tracker")
    #         print("1️⃣ Enter Logs for Today")
    #         print("2️⃣ View Logs History")
    #         print("3️⃣ View Analysis")
    #         print("4️⃣ Exit\n")

    #         choice = int(input("Enter your choice (1/2/3/4): "))

    #         if choice == 1:
    #             add_logs()
    #         elif choice == 2:
    #             view_history()
    #         elif choice == 3:
    #             analysis()
    #         elif choice == 4:
    #             break
    #         else:
    #             print("Invalid Choice. Please Try again.\n")