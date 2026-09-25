# infinite looping
while True:
    if input("Enter guess: ") == "Wow":
        break

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

# simple explanation for modulus
# 20 /3 => 6 sisa 2
# 20 % 3 => 2

# odd and even checker
# 1 / 2 = 0 sisa 1 => 1 % 2 = 1
# 3 / 2 = 1 sisa 1 => 3 % 2 = 1
# 5 / 2 = 2 sisa 1 => 5 % 2 = 1

# 2 / 2 = 1 sisa 0 => 2 % 2 = 0
# 4 / 2 = 2 sisa 0 => 4 % 2 = 0
# 6 / 2 = 3 sisa 0 => 6 % 2 = 0