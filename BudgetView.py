# fill this window with all the categories and u can view all the expenses
# on top make sure there is the total money left or budget
from tkinter import *
from tkinter import ttk
import datetime as dt
from tkinter import messagebox
import customtkinter



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        h1 = ('Arial', 70)
        h2 = ('Arial', 20)

        self.expense_total_frame = customtkinter.CTkFrame(self)
        self.expense_total_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")
        customtkinter.CTkLabel(self.expense_total_frame, 
            text="Total expenses", font=h2).grid(row=0, column=0, sticky=W, padx = 10)
        customtkinter.CTkLabel(self.expense_total_frame, 
            text=self.total_expenses_callback(), font=h1).grid(row=1, column=0, sticky=W, padx = 10)
        calc_button = customtkinter.CTkButton(
            self.expense_total_frame, 
            text='Calculate'
        )
        graph_button = customtkinter.CTkButton(
            self.expense_total_frame, 
            text='Graph'
        )
        calc_button.grid(row=2, column=0, sticky=EW, padx=(10, 0), pady=(10, 10))
        graph_button.grid(row=2, column=1, sticky=EW, padx=(10, 0), pady=(10, 10))
        

        self.remaining_budget_frame = customtkinter.CTkFrame(self)
        self.remaining_budget_frame.grid(row=0, column=1, padx=(10,10), pady=(10, 0), sticky="nsw")
        customtkinter.CTkLabel(self.remaining_budget_frame, 
            text="Remaining budget", font=h2).grid(row=0, column=0, sticky=W, padx = 10)
        customtkinter.CTkLabel(self.remaining_budget_frame, 
            text=self.remaining_budget_callback(), font=h1).grid(row=1, column=0, sticky=W, padx = 10)
        
        budgetVar = IntVar()
        self.budget_input_frame = customtkinter.CTkFrame(self)
        self.budget_input_frame.grid(row=1, column=1, padx=(10,10), pady=(10, 0), sticky="nsw")
        customtkinter.CTkLabel(self.budget_input_frame, 
            text="Budget input", font=h2).grid(row=0, column=0, sticky=W, padx = 10)
        self.budget_input = customtkinter.CTkEntry(self.budget_input_frame, textvariable=budgetVar)
        self.budget_input.grid(row=0, column=1, sticky=EW, padx=(10, 0))
        budget_button = customtkinter.CTkButton(
            self.budget_input_frame, 
            text='Save'
        )
        budget_button.grid(row=0, column=2, sticky=EW, padx=(10, 0), pady=(10, 10))
        
        
    def total_expenses_callback(self):
        return 5000
    
    def remaining_budget_callback(self):
        return 10000
    
app = App()
app.mainloop()