# string methods == functions that belong to string type
city = "vancouver"

# func() -> execute, call, run
print(city.capitalize())

upper = city.upper()
lower = city.lower()
print(upper)
print(lower)

# index(sub): returns the index of substring, but if it doesn't exist, error!
print(city.index("an"))
# print(city.index("xxx"))  # error

# find(sub): returns the index of the first occurrence of substring
#            no match will return -1
print(city.find("an"))
print(city.find("xxx"))  # -1

# count(sub[, start[, end]]): returns the occurrences of substring in string
# case-sensitive (o) vs case-insensitive (x)
greetings = "hello hello hello"
print(greetings.count("hello", 5, 12))

# (python official) https://docs.python.org/3/library/stdtypes.html
# https://www.w3schools.com/python/python_ref_string.asp
