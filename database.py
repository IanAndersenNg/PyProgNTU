import sqlite3

class Database:
    def __init__(self, db) -> None:
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS expense_record (item_name text, item_price float, purchase_date date, category text)")
        self.conn.commit()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS income_record (amount, date)")
        self.conn.commit()

    def fetchRecord(self, query):
        self.cur.execute(query)
        rows = self.cur.fetchall()
        return rows

    def insertExpense(self, item_name, item_price, purchase_date, category):
        self.cur.execute("INSERT INTO expense_record VALUES (?, ?, ?, ?)",
            (item_name, item_price, purchase_date, category))
        self.conn.commit()

    def removeExpense(self, rwid):
        self.cur.execute("DELETE FROM expense_record WHERE rowid=?", (rwid,))
        self.conn.commit()

    def updateExpense(self, item_name, item_price, purchase_date, category, rid):
        self.cur.execute("UPDATE expense_record SET item_name = ?, item_price = ?, purchase_date = ?, category = ? WHERE rowid = ?",
            (item_name, item_price, purchase_date, category, rid))
        self.conn.commit()

    def insertIncome(self, income_amount, income_date):
        self.cur.execute("INSERT INTO income_record VALUES (?, ?)",(income_amount, income_date))
        self.conn.commit()

    def updateBudget(self, budget_amount):
        self.cur.execute("UPDATE budget SET amount = ?  ",(budget_amount))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    