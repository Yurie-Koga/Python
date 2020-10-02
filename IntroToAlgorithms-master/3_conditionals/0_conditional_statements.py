# Conditional Statement (If-else statement)
# if __condition__:
#     do something
# elif __condition__:
#     do something
# else:
#     do something

age = int(input("Enter your age: "))

if age >= 18:
    print("You can start drinking...")
elif 15 <= age < 18:
    print("Highschool student")
elif 13 <= age < 15:
    print("Junior-highschool student")
elif 7 <= age < 13:
    print("Elementary school student")
elif 5 <= age < 7:
    print("Kindergarten")
else:
    print("Baby")
