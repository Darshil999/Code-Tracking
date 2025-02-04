import tkinter as tk
from starting import Code

window = tk.Tk()
window.title("Code Tracker")
window.geometry("700x600")

# Label
label = tk.Label(window, text="Welcome to Code Tracker", font=("Arial", 16))
label.grid(row=0, column=1, columnspan=2, pady=20)

# Buttons with Correct Command and Grid Layout
add_button = tk.Button(window, text="1️⃣ Enter Logs for Today", width=25, command=Code.add_logs)
view_button = tk.Button(window, text="2️⃣ View Logs History", width=25, command=Code.view_history)
analysis_button = tk.Button(window, text="3️⃣ View Analysis", width=25, command=Code.analysis)

add_button.grid(row=1, column=1, pady=10)
view_button.grid(row=2, column=1, pady=10)
analysis_button.grid(row=3, column=1, pady=10)

window.mainloop()
