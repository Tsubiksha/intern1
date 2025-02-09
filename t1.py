import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task.strip():
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a valid task!")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def on_enter(button, color):
    button.config(bg=color)

def on_leave(button, color):
    button.config(bg=color)

# Main application window
root = tk.Tk()
root.title("Interactive To-Do List")
root.geometry("400x500")
root.configure(bg="#ffe4b5")

# Header
header = tk.Label(
    root, text="To-Do List", font=("Helvetica", 24, "bold"), bg="#ffa07a", fg="white"
)
header.pack(fill="x", pady=10)

# Entry field
task_entry = tk.Entry(root, font=("Arial", 14), bg="#f5deb3", fg="#6a5acd")
task_entry.pack(pady=10, padx=10, fill="x")

# Buttons frame
button_frame = tk.Frame(root, bg="#ffe4b5")
button_frame.pack(pady=10)

# Add Task button
add_button = tk.Button(
    button_frame,
    text="Add Task",
    font=("Arial", 14, "bold"),
    bg="#98fb98",
    fg="#000000",
    activebackground="#32cd32",
    activeforeground="white",
    command=add_task,
)
add_button.grid(row=0, column=0, padx=10)

add_button.bind("<Enter>", lambda e: on_enter(add_button, "#32cd32"))
add_button.bind("<Leave>", lambda e: on_leave(add_button, "#98fb98"))

# Delete Task button
delete_button = tk.Button(
    button_frame,
    text="Delete Task",
    font=("Arial", 14, "bold"),
    bg="#ff7f7f",
    fg="#000000",
    activebackground="#ff4500",
    activeforeground="white",
    command=delete_task,
)
delete_button.grid(row=0, column=1, padx=10)

delete_button.bind("<Enter>", lambda e: on_enter(delete_button, "#ff4500"))
delete_button.bind("<Leave>", lambda e: on_leave(delete_button, "#ff7f7f"))

# Task list with a scrollbar
task_frame = tk.Frame(root, bg="#ffe4b5")
task_frame.pack(fill="both", expand=True, pady=10, padx=10)

task_scrollbar = tk.Scrollbar(task_frame)
task_scrollbar.pack(side="right", fill="y")

task_listbox = tk.Listbox(
    task_frame,
    font=("Arial", 14),
    bg="#fffacd",
    fg="#4682b4",
    selectbackground="#4682b4",
    selectforeground="white",
    yscrollcommand=task_scrollbar.set,
)
task_listbox.pack(fill="both", expand=True)

task_scrollbar.config(command=task_listbox.yview)

# Footer
footer = tk.Label(
    root,
    text="Stay Organized!",
    font=("Helvetica", 14, "italic"),
    bg="#ffa07a",
    fg="white",
)
footer.pack(fill="x", pady=5)

root.mainloop()
