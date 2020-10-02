# Data Types
# There are many different data types
# 1. int: integer
# 2. float: floating point (10.23, 3.1231, ...)
# 3. str: a sequence of characters in quotes "aa"
# 4. bool: boolean
# 5. list: ...
# ...

language = "en_us"
print(type(language))  # check the type of a variable using type()

users = 10
print(str(users) + language)  # "10" + "en_us" => "10en_us"

# Type conversion (type casting) : changing types
# There are several built-in functions that let you convert one data type
# to another.
#
# str(x): converts x to a string
# int(x): converts x to an integer
# float(x): converts x to a floating point number

print(int("12"))

# Exercise: what is the type of the following operations?
# 1. 10 / 2  -> float
print(type(10 / 2))

# 2. 10 // 2  -> int
print(type(10 // 2))

# 3. float(5) -> 5.0 float
print(float(5))
print(type(float(5)))
