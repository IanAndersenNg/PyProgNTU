from tkinter import *
import customtkinter
from IncomeInput import IncomeInput

class IncomeFrame(customtkinter.CTkFrame):
    def __init__(self, master, db):
        super().__init__(master)
        self.db = db

        h1 = ('Arial', 70)
        h2 = ('Arial', 20)

        self.monthOption = customtkinter.CTkOptionMenu(self,values=["01","02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"], 
            command=lambda _: self.update_income_label())
        self.yearOption = customtkinter.CTkOptionMenu(self,values=["2024", "2025", "2026"], 
            command=lambda _: self.update_income_label())
        self.incomeLabel = customtkinter.CTkLabel(self,text="Income Saved", font=h2)
        self.incomeSaved = customtkinter.CTkLabel(self, text=self.remaining_budget_callback(), font=h1)
        self.input_income_button = customtkinter.CTkButton(
            self,text='Input income', command = self.input_income
        )

        self.incomeLabel.grid(row=0, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        self.monthOption.grid(row=1, column=0, sticky=EW, padx=(10, 0), pady=(10, 10))
        self.yearOption.grid(row=1, column=1, sticky=EW, padx=(10, 0), pady=(10, 10))
        self.incomeSaved.grid(row=2, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        self.input_income_button.grid(row=3, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)

    def remaining_budget_callback(self):
        month = self.monthOption.get()
        year = self.yearOption.get()
        expense = self.db.getExpenses(month, year)
        income = self.db.getIncome(month, year)
        return income - expense

    def update_income_label(self):
        month = self.monthOption.get()
        year = self.yearOption.get()
        expense = self.db.getExpenses(month, year)
        income = self.db.getIncome(month, year)
        diff = income - expense
        color = "white"

        if(diff < 0):
            color = "red"
        elif(diff < 200):
            color = "yellow"
        else:
            color = "green"
        
        self.incomeSaved.configure(text=str(diff), text_color = color)

    def input_income(self):
        income_window = IncomeInput(self.db, self)