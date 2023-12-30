import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

 def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and pack the listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Create and pack the entry widget
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Create and pack the buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)
delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.RIGHT, padx=5)

# Run the Tkinter event loop
root.mainloop()
