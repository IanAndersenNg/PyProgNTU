from tkinter import *
import customtkinter
from ExpenseCategory import ExpenseCategory

total_expenses = 5000

class ExpenseFrame(customtkinter.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db

        h1 = ('Arial', 70)
        h2 = ('Arial', 20)
    
        self.monthOption = customtkinter.CTkOptionMenu(self,values=["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], 
            command=lambda _: self.update_expenses_label())
        self.yearOption = customtkinter.CTkOptionMenu(self,values=["2024", "2025", "2026"], 
            command=lambda _: self.update_expenses_label())
        self.expenseLabel = customtkinter.CTkLabel(self, text="Total expenses", font=h2)
        self.expense = customtkinter.CTkLabel(self, text=self.default_total_expenses_callback(), font=h1)
        self.graph_button = customtkinter.CTkButton(
            self,text='Group & Graph', command = lambda:ExpenseCategory(master)
        )

        self.expenseLabel.grid(row=0, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        self.monthOption.grid(row=1, column=0, sticky=EW, padx=(10, 0), pady=(10, 10))
        self.yearOption.grid(row=1, column=1, sticky=EW, padx=(10, 0), pady=(10, 10))
        self.expense.grid(row=2, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        self.graph_button.grid(row=3, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)

    def default_total_expenses_callback(self):
        month = self.monthOption.get()
        year = self.yearOption.get()
        expenses = self.db.getExpenses(month, year)
        return expenses
    
    def update_expenses_label(self):
        month = self.monthOption.get()
        year = self.yearOption.get()
        expense = self.db.getExpenses(month, year)
        self.expense.configure(text=str(expense))