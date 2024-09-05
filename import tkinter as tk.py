import tkinter as tk
from tkinter import messagebox

class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Expense Tracker")

        self.expenses = {
            "Transportation": [],
            "Groceries": [],
            "Car": [],
            "Education": [],
            "Gifts": [],
            "Healthcare": [],
            "Food & Drink": [],
            "Bills & Fees": []
        }

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Category selection
        self.category_label = tk.Label(self.root, text="Select Category:")
        self.category_label.grid(row=0, column=0, padx=10, pady=10)

        self.category_var = tk.StringVar(value="Transportation")
        self.category_menu = tk.OptionMenu(self.root, self.category_var, *self.expenses.keys())
        self.category_menu.grid(row=0, column=1, padx=10, pady=10)

        # Amount entry
        self.amount_label = tk.Label(self.root, text="Enter Amount:")
        self.amount_label.grid(row=1, column=0, padx=10, pady=10)

        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.grid(row=1, column=1, padx=10, pady=10)

        # Description entry
        self.description_label = tk.Label(self.root, text="Description:")
        self.description_label.grid(row=2, column=0, padx=10, pady=10)

        self.description_entry = tk.Entry(self.root)
        self.description_entry.grid(row=2, column=1, padx=10, pady=10)

        # Add Expense button
        self.add_button = tk.Button(self.root, text="Add Expense", command=self.add_expense)
        self.add_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        # Display Expenses button
        self.display_button = tk.Button(self.root, text="Display Expenses", command=self.display_expenses)
        self.display_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

        # Text box to display expenses
        self.expense_text = tk.Text(self.root, height=10, width=50)
        self.expense_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def add_expense(self):
        category = self.category_var.get()
        amount = self.amount_entry.get()
        description = self.description_entry.get()

        if not amount.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid amount")
            return

        amount = float(amount)
        self.expenses[category].append({"amount": amount, "description": description})

        self.amount_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        messagebox.showinfo("Success", f"Added {amount} to {category}")

    def display_expenses(self):
        self.expense_text.delete(1.0, tk.END)
        for category, expense_list in self.expenses.items():
            total = sum(exp["amount"] for exp in expense_list)
            self.expense_text.insert(tk.END, f"Category: {category}, Total: {total}\n")
            for exp in expense_list:
                self.expense_text.insert(tk.END, f"  - Amount: {exp['amount']}, Description: {exp['description']}\n")
            self.expense_text.insert(tk.END, "\n")

# Create the main window
root = tk.Tk()
app = ExpenseTrackerApp(root)
root.mainloop()