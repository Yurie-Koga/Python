# Operators
# +, -, *, / (float division)
# // (int division)
# % (modulo): 'mod' remainder
# ** (power)

print(10 / 2)  # 5.0
print(10 // 3)  # 3
print(10 % 3)  # 1
print(10 ** 3)  # 1000

# = : assignment operator
number = 7
number = number + 3  # increments number by 3

# += : increment operator
number += 2
print("number =", number)

# -= : decrement operator
number -= 2
print("number =", number)

# *= : multiply by
number *= 2
print("number =", number)

# /=, //= divide by
number //= 2
print("number =", number)

# Boolean Operators
# Boolean (bool) is a type of value that can only be True or False

# 1. Comparison
# == : equality (equal)
print(3 == 4)
# != : not equal to
print(3 != 4)

# > : greater than
# < : less than
# >= : greater than or equal to
# <= : less than or equal to
print(3 > 4)
print(3 <= 3)

# This is 'chained comparison' (python only)
# Check (3 < x) and (x < 5) at the same time
x = 4
print(3 < x < 5)

# A or B : either A or B has to be True, to return True
# A and B : both A and B have to be True, to return True
print((3 != 3) or (4 == 4))  # True
print((3 < x) and (x < 5))

# Exercise
num = 10
# print((num > 1) and (num / 0 == 0))
print((num > 10) and (num / 0 == 0))
print((num > 1) or (num / 0 == 0))
print(not (num > 10) or (num / 0 == 0))
print(not True)  # False
print(not False)  # True
