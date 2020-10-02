
def f(x):  # function header (prototype)
    # function body
    return x + 2


print(f(3))
print(f(5))
print(f(7))


def print_one():
    print(1)


print_one()
print_one()


def get_fullname(fn: str, ln: str) -> str:
    full = fn + " " + ln
    return full


print(get_fullname("Derrick", "Park"))
print(get_fullname("Leo", "Park"))
print(get_fullname("Sean", "Park"))
john = get_fullname("John", "Smith")
print(john)


def print_menu():
    print("====== Menu ======")
    print("| 1. Paella      |")
    print("| 2. Feijoada    |")
    print("| 3. Sushi       |")
    print("| 4. Samgyupsal  |")
    print("| 5. Ceviche     |")
    print("==================")


print_menu()
print_menu()
