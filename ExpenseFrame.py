from tkinter import *
from tkinter import ttk
import datetime as dt
from tkinter import messagebox
import customtkinter


class ExpenseFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        h1 = ('Arial', 70)
        h2 = ('Arial', 20)

        customtkinter.CTkLabel(self, text="Total expenses", font=h2).grid(row=0, column=0, sticky=W, padx = 10)
        customtkinter.CTkLabel(self, text=self.total_expenses_callback(), font=h1).grid(row=1, column=0, sticky=W, padx = 10)
        calc_button = customtkinter.CTkButton(
            self,text='Calculate'
        )
        graph_button = customtkinter.CTkButton(
            self,text='Graph'
        )
        calc_button.grid(row=2, column=0, sticky=EW, padx=(10, 0), pady=(10, 10))
        graph_button.grid(row=2, column=1, sticky=EW, padx=(10, 10), pady=(10, 10))

    def total_expenses_callback(self):
        return 5000