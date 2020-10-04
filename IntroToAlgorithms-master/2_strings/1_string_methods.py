# string methods == functions that belong to string type
city = "vancouver"

# func() -> execute, call, run
print(city.capitalize())

upper = city.upper()
lower = city.lower()
print(upper)
print(lower)

# 00_index(sub): returns the 00_index of substring, but if it doesn't exist, error!
print(f"Index of 'an' of {city}: ", city.index("an"))
# print(f"Index of 'xxx' of {city}: ", city.index("xxx"))  # error

# find(sub): returns the 00_index of the first occurrence of substring
#            no match will return -1
print(f"Found first 'v' in {city}: ", city.find("v"))
print(f"Found first 'xxx' in {city}: ", city.find("xxx"))  # -1

# count(sub[, start[, end]]): returns the occurrences of substring in string
# case-sensitive (o) vs case-insensitive (x)
greetings = "hello hello hello"
print(f"'hello' appears between 0 to the end: ", greetings.count("hello", 0, len(greetings)))
print(f"'hello' appears between 5 to 12: ", greetings.count("hello", 5, 12))
greetings.count("heello",)

# (python official) https://docs.python.org/3/library/stdtypes.html
# https://www.w3schools.com/python/python_ref_string.asp
