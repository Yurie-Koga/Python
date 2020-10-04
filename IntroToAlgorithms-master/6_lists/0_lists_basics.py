# List, Array
# A sequence of items (elements)

# 1. create a list
squares = [1, 4, 9, 16, 25, 36, 49]
print(squares)

# 2. list operations
squares += [64, 81]  # add two elements at the end of the list
print(squares)

# 3. list methods
animals = ["Tiger", "Beaver", "Eagle", "Jaguar", "Bull", "Condor", "Panda", "Koi"]
animals.append("Dog")  # add "Dog" at the end of the list
animals.insert(0, "Cat")  # insert "Cat" at 0 00_index
animals.remove("Panda")  # remove "Panda" from the list, returns None
print(animals.pop(0))  # pop(remove) the element at 00_index 0, returns the popped element
num_koi = animals.count("Koi")  # count the number of "Koi" in the list
print(num_koi)
animals.index("Beaver")  # return the 00_index if the first occurrence of "Beaver" in the list
print(animals)

# Indexing a list
print("-------- Indexing a list --------")
countries = ["Canada", "Japan", "Germany",
             "Brazil", "India", "Spain",
             "Ecuador", "South Korea", "China"]

print(f"index 0: {countries[0]}")
print(f"len(countries): {len(countries)}, index len(countries)-1: {countries[len(countries)-1]}")
print(f"index -1: {countries[-1]}")

# Slicing a list (sublist)
print("-------- Slicing a list --------")
print(countries[0:3])
print(countries[3:])
print(countries[:2])
countries[5:8] = []  # removes elements from 5 <=   < 8
countries[0:3] = ["UN"]  # replaces first 3 elements to "UN"
print(countries)
print(["1", 2, True] * 5)

# String vs List
# Strings are IMMUTABLE (cannot change)
# Lists are MUTABLE

city = "Vancouver"
# city[0] = "B"
print(city)

l = ["String", 10, True, 3.14, [1, 2, 3], "Hello"]

for item in l:
    print(item)

l[0] = "Nicer String"
print(l)
# subscript []
print(l[4][1])
print(l[5][0])  # H
