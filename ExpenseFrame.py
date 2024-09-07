from tkinter import *
from tkinter import ttk
import datetime as dt
from tkinter import messagebox
import customtkinter


class ExpenseFrame(customtkinter.CTk):
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