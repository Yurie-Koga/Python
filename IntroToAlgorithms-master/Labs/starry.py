# What does the code below do? Write a comment explaining each line for Drawing 1.

while True:
    n = int(input("Choose a number: "))

    # Drawing Example
    for row in range(n):  # for each row
        for column in range(row+1):  # for each column
            print('*', end='')  # print without newline at the end
        print()

    # Drawing 1
    # for each row from 0 to n - 1
    # way 1
    for row in range(n):
        # stars : 2 * row + 1
        print(" " * (n - row - 1), end='')
        # spaces: n - row 1
        print("*" * (2 * row + 1))
    # wya 2
    for row in range(n):
        for col in range(n - row - 1):
            print(" ", end='')
        for col in range(2 * row + 1):
            print("*", end='')
        print()

    
    # YOUR CODE BELOW (feel free to comment out previous drawings to make newer ones more clear)
    print('Draw1')
    maxCol = n * 2 - 1  #n=3: 5
    mid = round(maxCol / 2 ) + 1 #row=1: 
    #print(f"maxcol is {maxCol} and middle is {mid}")

    for row in range(n):
        i = 0
        left = mid - row  #n=3: 3
        right = mid + row #n=3: 3
        #print(f"'*' will be set {left} to {right}")
        
        while i < left:
            print(' ', end='')
            i += 1
        while left <= i <= right:
            print('*', end='')
            i += 1
        while i <= maxCol:
            print(' ', end='')
            i += 1
        print()


    # Drawing 2: 2 * i + 1
    print('Draw2')
    i = n   # decrease
    while i > 0:
        for column in range(i):
            print('*', end='')
        i -= 1
        print()

    # Backward 
    # way 1
    for row in range(7, 0, -1):
        print('*' * row)
    # way 2
    for row in range(7, 0, -1):
        for col in range(row):
            print('*', end='')
        print()

    # Drawing 3
    print('Draw3')
    for row in range(1, n // 2 + 2):
        print("*" * row)
    for row in range(n // 2, 0, -1):
        print("*" * row)

    # Drawing 4
    print('Draw4')
    # print(" " * (n - row - 1), end='')
    #     # spaces: n - row 1
    #     print("*" * (2 * row + 1))

    #way1
    for row in range(n // 2, -1, -1):
        print(' ' * (n // 2 - row), end='')
        print("*" * (2 * row + 1))

    for row in range(1, n // 2 + 1):
        print(' ' * (n // 2 - row), end='')
        print("*" * (2 * row + 1))
    
    #way2
    for row in range(n // 2, -1, -1):
        for col in range(n // 2 - row):
            print(' ', end='')
        for col in range(2 * row + 1):
            print("*", end='')
        print()

    for row in range(1, n // 2 + 1):
        for col in range(n // 2 - row):
            print(' ', end='')
        for col in range(2 * row + 1):
            print("*", end='')
        print()


    # Drawing 5
    #way1
    print('Draw5')
    for row in range(0, n // 2 + 1):
        print(" " * (n // 2 - row), end='')
        print("*" * (2 * row + 1))
    for row in range(1, n // 2 + 1):
        print(" " * row, end='')
        print("*" * (n - row * 2))
    #way2
    for row in range(0, n // 2 + 1):
        for col in range(n // 2 - row):
            print(" ", end='')
        for col in range(2 * row + 1):
            print("*",end='')
        print()
    for row in range(1, n // 2 + 1):
        for col in range(row):
            print(" ", end='')
        for col in range(n - row * 2):
            print("*",end='')
        print()
