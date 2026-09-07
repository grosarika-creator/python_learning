Item = input("Item: ")
Quantity = input("Quantity: ")
Price = input("Price: ")
Quantity=int(Quantity)
Price =int(Price)
# nama variable huruf kecil semua. Kalau ada huruf besar nanti jadi class

print(f"|{"Item":^10}|{"Quantity":^10}|{"Price":^10}|{"Total":^10}|")
print(f"|{Item:^10}|{Quantity:^10}|{Price:^10}|{Quantity * Price:^10}|")