import tkinter as tk
from starting import add_logs,view_history,analysis

window = tk.Tk()

window.title("Code Tracker")

window.geometry("700x600")


label = tk.Label(window, text="Welcome to Code Tracker", font=("Arial", 16))

# Pack the label into the window
label.pack(pady=20)

add_button = tk.Button(window, text="1️⃣ Enter Logs for Today", width=15, command=add_logs)
add_button1 = tk.Button(window, text="1️⃣ Enter Logs for Today", width=15, command=add_logs)
add_button2 = tk.Button(window, text="1️⃣ Enter Logs for Today", width=15, command=add_logs)
add_button3 = tk.Button(window, text="1️⃣ Enter Logs for Today", width=15, command=add_logs)




window.mainloop()
