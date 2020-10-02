favorite_food = "Noodles" "Meat"
print(favorite_food)

# 'in' operator
# To check whether a string contains a specific letter
# or a substring.

print("eat" in favorite_food)

# Escaping characters (\)
# \n: newline character
# \t: tab character
# \": double quote character
# \\: backslash character
# How to print a newline?
p = "He says, \"how are you?\"\nI'm good."
print(p)

phrase = """This is a really long string.
Triple-quoted strings are used to define
multi-line strings!
"""

print(phrase)

# String formatting
# Format Specifiers
# %d: digit (integer)
# %s: string
# %f: float

name = "Derrick"
city = "Vancouver"
message = "Hello, Pycharm! My name is %s. I live in %s" % (name, city)
print(message)

current_year = 2020
year = "It's %d!" % current_year
print(year)

salary1 = 75_000.12
salary2 = 5_000.50
salary3 = 35_000.50
print("My first salary as a software developer was %10.2f" % salary1)
print("%10.2f" % salary1)  # %-10.2 : left align, width 10, 2 digits after decimal point
print("%10.2f" % salary2)
print("%10.2f" % salary3)

# String interpolation (from python 3.6)
a = 3
b = 4
print(f"{a} x {b} = {a * b}")
