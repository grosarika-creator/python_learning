# # infinite looping
# while True:
#     if input("Enter guess: ") == "Wow":
#         break

#Bilangan Genap
for i in range(100):
    if i % 2 == 0:
        continue
    print ("current number: ", i)
print()
#Bilangan Ganjil
for i in range(100):
    if i % 2 != 0:
        continue
    print ("current number: ", i)