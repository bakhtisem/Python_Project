import json
import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Faylga yuklash va yuklash funksiyalari
FILENAME = "tasks.json"

def load_tasks():
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

# Vazifalar ro‘yxatini yuklash
tasks = load_tasks()

def add_task():
    task_text = task_entry.get()
    deadline = deadline_entry.get()
    if task_text:
        tasks.append({"task": task_text, "deadline": deadline, "done": False})
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END)
        deadline_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Xatolik", "Vazifa matnini kiriting!")

def mark_done():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["done"] = not tasks[index]["done"]
        save_tasks()
        update_listbox()

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        save_tasks()
        update_listbox()

def update_listbox():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["done"] else "❌"
        task_listbox.insert(tk.END, f"{status} {task['task']} ({task['deadline']})")

# GUI yaratish
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")

frame = tk.Frame(root)
frame.pack(pady=10)

task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

deadline_entry = tk.Entry(frame, width=15)
deadline_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(root, text="➕ Qo‘shish", command=add_task)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

mark_button = tk.Button(root, text="✅ Bajardim", command=mark_done)
mark_button.pack(pady=5)

delete_button = tk.Button(root, text="🗑️ O‘chirish", command=delete_task)
delete_button.pack(pady=5)

update_listbox()
root.mainloop()
