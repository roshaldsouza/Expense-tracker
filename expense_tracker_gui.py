import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILENAME = "expenses.csv"

# Create CSV file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Category", "Note"])

# Function to add expense
def add_expense():
    amount = amount_entry.get()
    category = category_entry.get()
    note = note_entry.get()

    if not amount or not category:
        messagebox.showerror("Error", "Amount and Category are required.")
        return

    try:
        float(amount)  # Validate amount is a number
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return

    with open(FILENAME, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([amount, category, note])

    amount_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    note_entry.delete(0, tk.END)

    messagebox.showinfo("Success", "Expense added successfully!")

# Function to view expenses
def view_expenses():
    top = tk.Toplevel(root)
    top.title("All Expenses")

    tree = ttk.Treeview(top, columns=("Amount", "Category", "Note"), show="headings")
    tree.heading("Amount", text="Amount")
    tree.heading("Category", text="Category")
    tree.heading("Note", text="Note")

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            tree.insert("", tk.END, values=row)

    tree.pack(fill="both", expand=True, padx=10, pady=10)

# Function to calculate total
def total_expense():
    total = 0
    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            total += float(row[0])
    messagebox.showinfo("Total Expense", f"₹{total:.2f}")

# ---------------- GUI SETUP -------------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x350")
root.configure(bg="#f0f0f0")

style = ttk.Style()
style.theme_use("clam")

# Title
title_label = tk.Label(root, text="💸 Expense Tracker", font=("Helvetica", 18, "bold"), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

# Form Frame
form_frame = tk.Frame(root, bg="#f0f0f0")
form_frame.pack(pady=10)

# Amount
tk.Label(form_frame, text="Amount (₹):", bg="#f0f0f0").grid(row=0, column=0, sticky="w")
amount_entry = ttk.Entry(form_frame, width=30)
amount_entry.grid(row=0, column=1, pady=5)

# Category
tk.Label(form_frame, text="Category:", bg="#f0f0f0").grid(row=1, column=0, sticky="w")
category_entry = ttk.Entry(form_frame, width=30)
category_entry.grid(row=1, column=1, pady=5)

# Note
tk.Label(form_frame, text="Note:", bg="#f0f0f0").grid(row=2, column=0, sticky="w")
note_entry = ttk.Entry(form_frame, width=30)
note_entry.grid(row=2, column=1, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

ttk.Button(button_frame, text="Add Expense", command=add_expense).grid(row=0, column=0, padx=5)
ttk.Button(button_frame, text="View Expenses", command=view_expenses).grid(row=0, column=1, padx=5)
ttk.Button(button_frame, text="Total Spent", command=total_expense).grid(row=0, column=2, padx=5)

# Run the app
root.mainloop()
