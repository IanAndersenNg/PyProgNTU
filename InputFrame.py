import customtkinter
import tkinter as tk

class InputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        name_label = customtkinter.CTkLabel(self, text='Item name').grid(row=0, column=0, sticky='w', padx=20)
        price_label = customtkinter.CTkLabel(self, text='Item price').grid(row=1, column=0, sticky='w', padx=20)
        purchase_label = customtkinter.CTkLabel(self, text='Purchase date').grid(row=2, column=0, sticky='w', padx=20)

        item_name =  customtkinter.CTkEntry(self)
        item_amt =  customtkinter.CTkEntry(self, textvariable=tk.IntVar())
        transaction_date =  customtkinter.CTkEntry(self, textvariable=tk.StringVar())

        item_name.grid(row=0, column=1, sticky='ew', padx=(10, 0), pady=(10, 0))
        item_amt.grid(row=1, column=1, sticky='ew', padx=(10, 0), pady=(10, 0))
        transaction_date.grid(row=2, column=1, sticky='ew', padx=(10, 0), pady=(10, 10))

        cur_date = customtkinter.CTkButton(
            self, text='Current Date', command=None, width=15
        )

        submit_btn = customtkinter.CTkButton(
            self,
            text='Save Record', 
            command=None, 
        )

        clr_btn = customtkinter.CTkButton(
            self,
            text='Clear Entry', 
            command=None
        )

        quit_btn = customtkinter.CTkButton(
            self,
            text='Exit', 
            command=None, 
        )

        total_bal = customtkinter.CTkButton(
            self,
            text='Total Balance',
            command=None
        )

        total_bal = customtkinter.CTkButton(
            self,
            text='Total Balance',
            command=None
        )

        total_spent = customtkinter.CTkButton(
            self,
            text='Total Spent',
            command=None
        )

        update_btn = customtkinter.CTkButton(
            self,
            text='Update',
            command=None
        )

        del_btn = customtkinter.CTkButton(
            self,
            text='Delete',
            command=None
        )


        cur_date.grid(row=3, column=1, sticky='ew', padx=(10, 0), pady=(0,10))
        submit_btn.grid(row=0, column=2, sticky='ew', padx=(10, 0))
        clr_btn.grid(row=1, column=2, sticky='ew', padx=(10, 0))
        quit_btn.grid(row=2, column=2, sticky='ew', padx=(10, 0))
        total_bal.grid(row=0, column=3, sticky='ew', padx=(10, 20))
        update_btn.grid(row=1, column=3, sticky='ew', padx=(10, 20))
        del_btn.grid(row=2, column=3, sticky='ew', padx=(10, 20))
