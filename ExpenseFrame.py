from tkinter import *
import customtkinter


total_expenses = 5000

class ExpenseFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        h1 = ('Arial', 70)
        h2 = ('Arial', 20)
    
        expenseLabel = customtkinter.CTkLabel(self, text="Total expenses", font=h2)
        expense = customtkinter.CTkLabel(self, text=self.total_expenses_callback(), font=h1)
        monthOption = customtkinter.CTkOptionMenu(self,values=["January", "February", "March"])
        yearOption = customtkinter.CTkOptionMenu(self,values=["2024", "2025", "2026"])
        graph_button = customtkinter.CTkButton(
            self,text='Group & Graph'
        )

        expenseLabel.grid(row=0, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        monthOption.grid(row=1, column=0, sticky=EW, padx=(10, 0), pady=(10, 10))
        yearOption.grid(row=1, column=1, sticky=EW, padx=(10, 0), pady=(10, 10))
        expense.grid(row=2, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        graph_button.grid(row=3, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)

    def total_expenses_callback(self):
        return total_expenses