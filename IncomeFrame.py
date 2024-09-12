from tkinter import *
import customtkinter
from IncomeInput import IncomeInput

class IncomeFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        h1 = ('Arial', 70)
        h2 = ('Arial', 20)

        incomeLabel = customtkinter.CTkLabel(self,text="Income Saved", font=h2)
        incomeSaved = customtkinter.CTkLabel(self, text=self.remaining_budget_callback(), font=h1)
        monthOption = customtkinter.CTkOptionMenu(self,values=["January", "February", "March"])
        yearOption = customtkinter.CTkOptionMenu(self,values=["2024", "2025", "2026"])
        input_income_button = customtkinter.CTkButton(
            self,text='Input income', command = self.input_income
        )
        
        incomeLabel.grid(row=0, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        monthOption.grid(row=1, column=0, sticky=EW, padx=(10, 0), pady=(10, 10))
        yearOption.grid(row=1, column=1, sticky=EW, padx=(10, 0), pady=(10, 10))
        incomeSaved.grid(row=2, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)
        input_income_button.grid(row=3, column=0, sticky=EW, padx=(10, 0), pady=(10, 10), columnspan = 2)

    def remaining_budget_callback(self):
        return 10000
    
    def input_income(master):
        income_window = IncomeInput(master)