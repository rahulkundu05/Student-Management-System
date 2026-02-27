import tkinter as tk
from tkinter import messagebox

FILE_NAME = "students.xlsx"

def add_student():
    sid = entry_id.get()
    name = entry_name.get()
    dept = entry_dept.get()
    marks = entry_marks.get()

    if sid == "" or name == "" or dept == "" or marks == "":
        messagebox.showwarning("Input Error", "All fields are required")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"Student ID:{sid}\nStudent Name:{name}\nStudents Dept.:{dept}\nObtain Marks:{marks}\n")

    messagebox.showinfo("Success", "Student Added Successfully")
    clear_entries()
    view_students()

def view_students():
    listbox.delete(0, tk.END)
    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                listbox.insert(tk.END, line.strip())
    except FileNotFoundError:
        pass

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Error", "Select a student to delete")
        return

    data = listbox.get(selected)
    listbox.delete(selected)

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for line in lines:
            if line.strip() != data:
                file.write(line)

    messagebox.showinfo("Deleted", "Student Record Deleted")

def update_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("Select Error", "Select a student to update")
        return

    updated_data = f"{entry_id.get()},{entry_name.get()},{entry_dept.get()},{entry_marks.get()}"

    with open(FILE_NAME, "r") as file:
        lines = file.readlines()

    with open(FILE_NAME, "w") as file:
        for i, line in enumerate(lines):
            if i == selected[0]:
                file.write(updated_data + "\n")
            else:
                file.write(line)

    messagebox.showinfo("Updated", "Student Record Updated")
    clear_entries()
    view_students()

def clear_entries():
    entry_id.delete(0, tk.END)
    entry_name.delete(0, tk.END)
    entry_dept.delete(0, tk.END)
    entry_marks.delete(0, tk.END)

# ---------------- GUI ----------------

root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

tk.Label(root, text="Student ID").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Name").grid(row=1, column=0, padx=10, pady=5)
tk.Label(root, text="Department").grid(row=2, column=0, padx=10, pady=5)
tk.Label(root, text="Marks").grid(row=3, column=0, padx=10, pady=5)

entry_id = tk.Entry(root)
entry_name = tk.Entry(root)
entry_dept = tk.Entry(root)
entry_marks = tk.Entry(root)

entry_id.grid(row=0, column=1)
entry_name.grid(row=1, column=1)
entry_dept.grid(row=2, column=1)
entry_marks.grid(row=3, column=1)

tk.Button(root, text="Add Student", command=add_student, width=15).grid(row=4, column=0, pady=10)
tk.Button(root, text="Update Student", command=update_student, width=15).grid(row=4, column=1)
tk.Button(root, text="Delete Student", command=delete_student, width=15).grid(row=5, column=0)
tk.Button(root, text="Clear", command=clear_entries, width=15).grid(row=5, column=1)

listbox = tk.Listbox(root, width=60)
listbox.grid(row=6, column=0, columnspan=2, padx=10, pady=20)

view_students()

root.mainloop()
