import customtkinter
import tkinter as tk
from tkinter import *
from tkinter import ttk
from InputFrame import InputFrame
from OutputFrame import OutputFrame

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Budget Planner")

        self.output_frame = OutputFrame(self)
        self.output_frame.grid(row=0, column=0, padx=(40,40), pady=(40, 40))

        self.input_frame = InputFrame(self)
        self.input_frame.grid(row=1, column=0, padx=10, pady=(10, 0))
        # self.input_frame.pack(expand=True, fill='both', padx=40, pady=40)


budget_planner_app = App()
budget_planner_app.mainloop()


