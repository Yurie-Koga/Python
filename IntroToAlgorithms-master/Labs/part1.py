

def get_1(n, number):
    # way 1: loop to cut off
    # 123456789     -> 12345678.9   -> 12345678 (// 10)
    # 12345678      -> 1234567.8    -> 1234567  (// 10)
    # 1234567       -> 123456.7     -> 7        (% 10)
    while n > 1:    # divide by 10 till n=1, then mod
        number = number // 10
        n -= 1
    print(number % 10)
    i = 1
    while i < n:
        number = number // 10
        i += 1
    print(number % 10)

def get_2(n, number):
    # way 2: use length
    s = str(number)
    print(f"len: {len(s)}, len-n: {len(s)-n}")
    print(s[len(s) - n])    # 9-3=6

def get_3(n, number):
    # way 3:
    print(f"10 ** (n-1): {10 ** (n-1)}")    # divide by 10 till n=1, then mod
    print((number // 10 ** (n-1)) % 10)

while True:  # This makes your code repeat forever,
    # to make it easier for you to keep testing it out with different values

    # You may assume the input will be valid
    # e.g. Your program does not have to work if someone gives an n that is
    #      bigger than the total number of digits in number. Your code must
    #      only work correctly for valid input.
    number = int(input("Please give an integer number: "))  # this asks the user for input and then stores the user
    # input as an int into our variable.
    n = int(input("Which position's digit do you want? "))

    print(".....YOUR CODE HERE......")  # TODO: Replace the filler text here with your code

    print("----Get 1----")
    get_1(n, number)
    print("----Get 2----")
    get_2(n, number)
    print("----Get 3----")
    get_3(n, number)

    # input: 123456789
    # target: 3
    # output: 7


