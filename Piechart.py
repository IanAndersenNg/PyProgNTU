import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import ExpenseCategory as ExpTrack


def get_expense(expense_tracker):
    expense={}
    for category, expense_list in expense_tracker.expenses.items():
        total = sum(exp["amount"] for exp in expense_list)
        expense[category]=total
    return expense
    

def draw_graph(expense_tracker):
    # Create the main tkinter window
    chart_window = tk.Toplevel()
    chart_window.title("Pie Chart for expense breakdown")

    # Create a frame for the pie chart
    frame = ttk.Frame(chart_window)
    frame.pack(fill=tk.BOTH, expand=True)

    # Get the expense data from the expense_tracker
    expense=get_expense(expense_tracker)    
    labels=list(expense.keys())
    sizes=list(expense.values())
    colors = ['purple', 'yellowgreen', 'lightblue', 'yellow','pink','red','blue','green']
    filtered_labels = [label for i, label in enumerate(labels) if sizes[i] > 0]
    filtered_sizes = [size for size in sizes if size > 0]
    filtered_colors = [color for i, color in enumerate(colors) if sizes[i] > 0]

    # Check if there are expenses to display
    if not filtered_sizes:
        tk.messagebox.showinfo("No Expenses", "No expenses to display in the pie chart.")
        chart_window.destroy()
        return

    explode = [0 for _ in filtered_sizes]
    # Create the pie chart using matplotlib
    fig, ax = plt.subplots()
    #ax.pie(filtered_sizes, labels=filtered_labels, colors=filtered_colors, autopct='%1.1f%%', startangle=90,explode=explode)
    wedges, texts, autotexts = ax.pie(filtered_sizes, labels=filtered_labels, colors=filtered_colors,
                                    autopct='%1.1f%%', startangle=90, explode=explode)
    ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    ax.legend(title="Expense breakdown:")
    # Embed the matplotlib figure in the tkinter window

    # Function to update the explode values when the mouse hovers
    def on_hover(event):
        if event.inaxes == ax:
            for i, wedge in enumerate(wedges):
                if wedge.contains_point([event.x, event.y]):
                    explode = [0] * len(filtered_sizes)
                    explode[i] = 0.2 
                    ax.clear()
                    ax.pie(filtered_sizes, labels=filtered_labels, colors=filtered_colors,
                        autopct='%1.1f%%', startangle=90, explode=explode)
                    ax.legend(title="Expense breakdown:")
                    fig.canvas.draw()

    # Connect the hover event to the function
    fig.canvas.mpl_connect('motion_notify_event', on_hover)

    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
