# Tuples are almost identical to lists.
# The only big difference between lists and tuples is that
# tuples cannot be modified (immutable).
# Tuples, you can NOT add(append), change(replace), or delete(remove)
# elements from the tuple.

# Tuples = "Immutable Lists"
vowels = ("a", "e", "i", "o", "u")
print(vowels[0])
print("k" in vowels)
# vowels[0] = "A"  # Error!

# Methods
vowels.index("e")
vowels.count("i")

# Use cases
# 1. return multiple values from a function


def split_name(name: str) -> (str, str):
    fullname = name.split(" ")
    first = fullname[0]
    last = fullname[1]

    return first, last


# 2. multiple assignments (_ to ignore)
fn, ln = split_name("Derrick Park")
print(ln)
print(fn)


# 3. constant list of data
livable_provinces = ("BC", "ON", "AB", "QC")

# swap!
a = 10
b = 20

temp = a
a = b
b = temp

print(a)  # a = 20
print(b)  # b = 10

# only python way!
x = 50
y = 70

x, y = y, x
print(x)
print(y)


def split_names(*names):
    print(names)


split_names("Jiro")
split_names("Carlos", "Martinez", "Rodrigo", "Santos")
