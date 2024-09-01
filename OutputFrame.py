import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter import *

class OutputFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        tv = ttk.Treeview(self, selectmode='browse', columns=(1, 2, 3, 4), show='headings', height=8, )
        tv.pack(side="left")

        tv.column(1, anchor=CENTER, stretch=NO, width=70)
        tv.column(2, anchor=CENTER)
        tv.column(3, anchor=CENTER)
        tv.column(4, anchor=CENTER)
        tv.heading(1, text="Serial no")
        tv.heading(2, text="Item Name", )
        tv.heading(3, text="Item Price")
        tv.heading(4, text="Purchase Date")

        style = ttk.Style()
        style.theme_use("default")
        style.map("Treeview")

        #12 scrollbar widget
        scrollbar = Scrollbar(self, orient='vertical')
        scrollbar.configure(command=tv.yview)
        scrollbar.pack(side="right", fill="y")
        tv.config(yscrollcommand=scrollbar.set)
