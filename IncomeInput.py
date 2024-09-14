
# import modules 
from tkinter import *
from Database import Database
import customtkinter
import re
from tkinter import messagebox


class IncomeInput(customtkinter.CTkToplevel):
    def __init__(self, db, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.db = db

        h2 = ('Arial', 14)

        self.budget_input_frame = customtkinter.CTkFrame(self)
        self.budget_input_frame.grid(row=0, column=0, padx=(10,10), pady=(20, 20), sticky="nsw")

        customtkinter.CTkLabel(self.budget_input_frame, 
            text="Income date", font=h2).grid(row=1, column=0, sticky=W, padx = 10)
        customtkinter.CTkLabel(self.budget_input_frame, 
            text="Income input", font=h2).grid(row=0, column=0, sticky=W, padx = 10)
        self.budget_input = Entry(self.budget_input_frame)
        self.date_input = Entry(self.budget_input_frame)

        self.budget_input.grid(row=0, column=1, sticky=EW, padx=(10, 0))
        self.date_input.grid(row=1, column=1, sticky=EW, padx=(10, 0), pady = (0,10))

        budget_button = customtkinter.CTkButton(
            self.budget_input_frame, text='Save',
            command =lambda: self.saveRecord(self.budget_input.get(), self.date_input.get())
        )
        budget_button.grid(row=0, column=2, sticky=EW, padx=(10, 10), pady=(10, 10))
        
    def saveRecord(self, income_amount, income_date):

        try:
            if not re.match(r'^\d{2}-\d{2}-\d{4}$', income_date):
                raise ValueError("Date format should be dd-mm-yyyy")
            
            if not income_amount.isdigit():
                raise ValueError("income amount must be digit")
            
            self.db.insertIncome(income_amount, income_date)
        except ValueError as e:
            messagebox.showerror("Invalid Date", str(e))         


        
        