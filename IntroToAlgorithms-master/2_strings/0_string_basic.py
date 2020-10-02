# String (str) : A sequence of characters in "" or ''

# + (concatenation) : combining two strings
print("Hello" + " World")

# * (multiplication) : repeating strings
print("Hello" * 10)

# String indexing (position)
singer = "Lady Gaga"
# index   012345678
print(singer[0])  # "L"
# print(singer[9])  # IndexError: string index out of range
print(singer[-1])  # the last character
print(singer[-5])  # " "

# string slicing (substring)
# s[start:end]   start <=    < end
print(singer[0:2])  # "La"

actor = "Clint Eastwood"
#        01234567890123
print(actor[0:5])  # "Clint"
print(actor[:5])  # "Clint"
print(actor[5:])  # " Eastwood"
print(actor[:])  # a copy of actor

# How to get the total number of chars?
# len()
print(len(actor))
print(actor[len(actor) - 1])  # last char
print(actor[-1])  # last char
