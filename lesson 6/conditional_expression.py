# normal code
country = input("Enter a country: ").lower()
if country == "indonesia": status = True
else: status = False
print("status:", status)

# syntactic sugar
status2 = True if country == 'indonesia' else False
print("status:", status2)