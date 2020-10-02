# Write a program that takes an user input for an exam mark, and prints
# the grade for that mark - according to the following scheme:
#
#
#   Mark      Grade
#   >= 90       A
#  [80-90)      B
#  [70-80)      C
#  [60-70)      D
#    < 60       F
#
#
# The square and round brackets denote closed and open intervals(range).
# A closed interval includes the number, and open interval excludes it.
# Test your program by print the mark and the grade for a number of different marks.

mark = int(input("Enter your mark: "))

if mark >= 90:
    print("A")
elif mark >= 80:
    print("B")
elif mark >= 70:
    print("C")
elif mark >= 60:
    print("D")
else:
    print("F")