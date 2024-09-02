import statistics
Money_saved_list=[]
Target_item = str(input("Please enter the item you want to save money for:"))
Price_item = float(input("Please enter the price of the item you want to save money for(Unit: SGD):"))
num_days = int(input("Please enter total days (unit: days):")) 
for i in range (num_days):
    amount = float(input(f"Please enter the amount of money deposited in {i+1} days (Unit: SGD):"))
    Money_saved_list.append(amount)
Required_days = (Price_item-sum(Money_saved_list))/(statistics.mean(Money_saved_list))
print("Approximate number of days it will take to purchase this item(Unit: Days):",Required_days)