print("Invoice App")

item = input("Item: ")
quantity = int(input("Quantity: "))
price = int(input("Price: "))

header = f"|{'Item':^10}|{'Quantity':^10}|{'Price':^10}|{'Total':^10}|"
separator = "-" * len(header)
row_data = f"|{item:^10}|{quantity:^10}|{price:^10}|{(quantity * price):^10}|"

print(separator)
print(header)
print(separator)
print(row_data)
print(separator)

# Question: Gimana caranya agar pada price ada separator . atau , ?