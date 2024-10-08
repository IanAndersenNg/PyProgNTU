# import modules 
from tkinter import *
from tkinter import ttk
import datetime as dt
from Database import *
from tkinter import messagebox
import customtkinter

data = Database(db='test.db')
count = 0
selected_rowid = 0


def saveRecord():
    global data
    data.insertRecord(item_name=item_name.get(), item_price=item_amt.get(), purchase_date=transaction_date.get())
       
def setDate():
    date = dt.datetime.now()
    dopvar.set(f'{date:%d %B %Y}')

def clearEntries():
    item_name.delete(0, 'end')
    item_amt.delete(0, 'end')
    transaction_date.delete(0, 'end')

def fetch_records():
    f = data.fetchRecord('select rowid, * from expense_record')
    global count
    for rec in f:
        tv.insert(parent='', index='0', iid=count, values=(rec[0], rec[1], rec[2], rec[3]))
        count += 1
    tv.after(400, refreshData)

def select_record(event):
    global selected_rowid
    selected = tv.focus()    
    val = tv.item(selected, 'values')
  
    try:
        selected_rowid = val[0]
        d = val[3]
        namevar.set(val[1])
        amtvar.set(val[2])
        dopvar.set(str(d))
    except Exception as ep:
        pass


def update_record():
    global selected_rowid
    selected = tv.focus()
	# Update record
    try:
        data.updateRecord(namevar.get(), amtvar.get(), dopvar.get(), selected_rowid)
        tv.item(selected, text="", values=(namevar.get(), amtvar.get(), dopvar.get()))
    except Exception as ep:
        messagebox.showerror('Error',  ep)

	# Clear entry boxes
    item_name.delete(0, END)
    item_amt.delete(0, END)
    transaction_date.delete(0, END)
    tv.after(400, refreshData)
    

def totalBalance():
    f = data.fetchRecord(query="Select sum(item_price) from expense_record")
    for i in f:
        for j in i:
            messagebox.showinfo('Current Balance: ', f"Total Expense: ' {j} \nBalance Remaining: {5000 - j}")

def refreshData():
    for item in tv.get_children():
      tv.delete(item)
    fetch_records()
    
def deleteRow():
    global selected_rowid
    data.removeRecord(selected_rowid)
    refreshData()

ws = Tk()
ws.title('Daily Expenses')


f = ('Arial', 14)
namevar = StringVar()
amtvar = IntVar()
dopvar = StringVar()

f1 = customtkinter.CTkFrame(ws)
f1.grid(row=1, column=1, padx = 50, pady = 20)


customtkinter.CTkLabel(f1, text='Expense name', font=f).grid(row=0, column=0, sticky=W, padx = 10)
customtkinter.CTkLabel(f1, text='Expense amount', font=f).grid(row=1, column=0, sticky=W, padx = 10)
customtkinter.CTkLabel(f1, text='Purchase date', font=f).grid(row=2, column=0, sticky=W, padx = 10)


item_name = customtkinter.CTkEntry(f1, font=f, textvariable=namevar)
item_amt = customtkinter.CTkEntry(f1, font=f, textvariable=amtvar)
transaction_date = customtkinter.CTkEntry(f1, font=f, textvariable=dopvar)

item_name.grid(row=0, column=1, sticky=EW, padx=(10, 0))
item_amt.grid(row=1, column=1, sticky=EW, padx=(10, 0))
transaction_date.grid(row=2, column=1, sticky=EW, padx=(10, 0))


# Action buttons
cur_date = customtkinter.CTkButton(
    f1, 
    text='Current Date', 
    command=setDate,
    width=15
)

submit_btn = customtkinter.CTkButton(
    f1, 
    text='Save Record', 
    command=saveRecord
)

clr_btn = customtkinter.CTkButton(
    f1, 
    text='Clear Entry', 
    command=clearEntries
)

quit_btn = customtkinter.CTkButton(
    f1, 
    text='Exit', 
    command=lambda:ws.destroy()
)

total_bal = customtkinter.CTkButton(
    f1,
    text='Total Balance',
    command=totalBalance
)

total_spent = customtkinter.CTkButton(
    f1,
    text='Total Spent',
    command=lambda:data.fetchRecord('select sum(ite)')
)

update_btn = customtkinter.CTkButton(
    f1, 
    text='Update',
    command=update_record
)

del_btn = customtkinter.CTkButton(
    f1, 
    text='Delete',
    command=deleteRow
)

cur_date.grid(row=3, column=1, sticky=EW, padx=(10, 0), pady=(10, 0))
submit_btn.grid(row=0, column=2, sticky=EW, padx=(10, 0), pady=(10, 0))
clr_btn.grid(row=1, column=2, sticky=EW, padx=(10, 0), pady=(10, 0))
quit_btn.grid(row=2, column=2, sticky=EW, padx=(10, 0), pady=(10, 0))
total_bal.grid(row=0, column=3, sticky=EW, padx=(10, 0), pady=(10, 0))
update_btn.grid(row=1, column=3, sticky=EW, padx=(10, 0), pady=(10, 0))
del_btn.grid(row=2, column=3, sticky=EW, padx=(10, 0), pady=(10, 0))

f2 = customtkinter.CTkFrame(ws)
f2.grid(row=0, column=1, padx = 20, pady = 20)

# Treeview widget
tv = ttk.Treeview(f2, columns=(1, 2, 3, 4), show='headings', height=8)
tv.pack(side="left")

# add heading to treeview
tv.column(1, anchor=CENTER, stretch=NO, width=70)
tv.column(2, anchor=CENTER)
tv.column(3, anchor=CENTER)
tv.column(4, anchor=CENTER)
tv.heading(1, text="Serial no")
tv.heading(2, text="Item Name", )
tv.heading(3, text="Item Price")
tv.heading(4, text="Purchase Date")

# binding treeview
tv.bind("<ButtonRelease-1>", select_record)

# style for treeview
style = ttk.Style()
style.theme_use("default")
style.map("Treeview")

# Vertical scrollbar
scrollbar = Scrollbar(f2, orient='vertical')
scrollbar.configure(command=tv.yview)
scrollbar.pack(side="right", fill="y")
tv.config(yscrollcommand=scrollbar.set)

# calling function 
fetch_records()

# infinite loop
ws.mainloop()
