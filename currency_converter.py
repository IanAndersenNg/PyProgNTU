import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests

# URL网址
URL = "https://api.exchangerate-api.com/v4/latest/USD"

# 定义获取汇率的功能函数
def get_exchangerate():
    try:
        response = requests.get(URL)
        response.raise_for_status()  # 检查请求是否成功
        data = response.json()
        if 'rates' in data:
            return data['rates']
        else:
            messagebox.showerror("Data Error", "Error in API response format")
            return {}
    except requests.RequestException as e:
        messagebox.showerror("API Error", f"Error fetching data from API: {e}")
        return {}

# 展示实时汇率tree
def update_ratestable():
    rates = get_exchangerate()
    if rates:
        major_currencies = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "MXN",
                            "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "INR", "BRL", "ZAR"]

        for row in tree.get_children():
            tree.delete(row)

        chinese_names = {"USD": "美元", "EUR": "欧元", "JPY": "日本元", "GBP": "英镑", "AUD": "澳大利亚元",
                         "CAD": "加拿大元", "CHF": "瑞士法郎", "CNY": "人民币", "SEK": "瑞典克朗",
                         "NZD": "新西兰元", "MXN": "墨西哥比索", "SGD": "新加坡元", "HKD": "港币",
                         "NOK": "挪威克朗", "KRW": "韩币", "TRY": "土耳其里拉", "RUB": "俄罗斯卢布",
                         "INR": "印度卢比", "BRL": "巴西雷亚尔", "ZAR": "南非兰特"}

        for currency in major_currencies:
            rate = rates.get(currency, "N/A")
            chinese_name = chinese_names.get(currency, "未知")
            tree.insert("", tk.END, values=(currency, chinese_name, "{:.2f}".format(rate) if rate != "N/A" else "N/A"))
    else:
        messagebox.showerror("Data Error", "Error loading exchange rates")

# 货币换算功能
def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_combobox.get()
        to_currency = to_currency_combobox.get()
        rates = get_exchangerate()
        if not rates:
            return

        if from_currency == to_currency:
            result = amount
        else:
            amount_usd = amount / rates[from_currency]
            result = amount_usd * rates[to_currency]

        result_label.config(text="{:.2f} {} = {:.2f} {}".format(amount, from_currency, result, to_currency))

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# 创建主窗口
root = tk.Tk()  # 创建主窗口
root.title("Currency Converter")  # 主窗口标题

# 创建主框架
main_frame = tk.Frame(root, padx=50, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# 创建“汇率转换器”框架
currency_converter_frame = tk.Frame(main_frame)
currency_converter_frame.pack(fill=tk.BOTH, expand=True)

# 创建“汇率展示”框架
exchange_rates_frame = tk.Frame(currency_converter_frame)
exchange_rates_frame.pack(pady=5, fill=tk.BOTH, expand=False)

# “汇率展示”标题
title_label = tk.Label(exchange_rates_frame, text="Current Exchange Rates", font=("Arial", 16))  # 设置标题和字体大小
title_label.pack(pady=5)

# 创建滚动条框架
table_frame = tk.Frame(exchange_rates_frame)
table_frame.pack(fill=tk.BOTH, expand=True)

# 创建 treeview 表
columns = ("Currency Name", "Chinese Name", "Exchange Rate")
tree = ttk.Treeview(table_frame, columns=columns, show='headings')
tree.heading("Currency Name", text="Currency Name")
tree.heading("Chinese Name", text="Chinese Name")
tree.heading("Exchange Rate", text="Exchange Rate")
tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 创建 treeview 的滚动条
scrollbar = tk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree.configure(yscrollcommand=scrollbar.set)

# 更新表格
update_ratestable()

# 创建“汇率计算”框架
conversion_frame = tk.Frame(currency_converter_frame)
conversion_frame.pack(pady=5, fill=tk.X, expand=False)

# 下拉列表
currency_row = tk.Frame(conversion_frame)
currency_row.pack(pady=5)

major_currencies = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD",
                    "MXN", "SGD", "HKD", "NOK", "KRW", "TRY", "RUB", "INR", "BRL", "ZAR"]
major_currencies_sorted = sorted(major_currencies)

tk.Label(currency_row, text="From Currency:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
from_currency_combobox = ttk.Combobox(currency_row, values=major_currencies_sorted, state="readonly")
from_currency_combobox.grid(row=0, column=1, padx=5, pady=5)
from_currency_combobox.set("USD")

tk.Label(currency_row, text="To Currency:").grid(row=0, column=2, padx=5, pady=5, sticky='e')
to_currency_combobox = ttk.Combobox(currency_row, values=major_currencies_sorted, state="readonly")
to_currency_combobox.grid(row=0, column=3, padx=5, pady=5)
to_currency_combobox.set("EUR")

# 数量，计算
amount_row = tk.Frame(conversion_frame)
amount_row.pack(pady=5)

tk.Label(amount_row, text="Amount:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
amount_entry = tk.Entry(amount_row)
amount_entry.grid(row=0, column=1, padx=5, pady=5)

convert_button = tk.Button(amount_row, text="Convert", command=convert_currency)
convert_button.grid(row=0, column=2, padx=5, pady=5, sticky='e')

result_label = tk.Label(amount_row, text="Result display")
result_label.grid(row=0, column=3, padx=5, pady=5)


root.mainloop()















