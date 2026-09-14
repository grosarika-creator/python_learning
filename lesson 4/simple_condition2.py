# < 50 => D
# 50 - 70 => C
# 71 - 80 => B
# > 81 => A 

score = int(input('Enter your score: '))

# cheat code: if you want to use <, 
# then compare from the least value

# cheat code: if you want to use >, 
# then compare from the largest value

# version 1
# if score < 50:
#     print("D")
# elif score >= 50 and score <= 70:
#     print("C")
# elif score >= 71 and score <=80:
#     print("B")
# else:
#     print("A")

# version 2
if score < 50:
    print('D')
elif score <= 70:
    print('C')
elif score <= 80:
    print('B')
else:
    print('A')

# wrong way:
if score <= 80:
    print('B')
elif score <= 70:
    print('C')
else:
    print('D')
# kalau mau pakai tanda < inget diurut dari yang paling kecil!! Vice versa.

