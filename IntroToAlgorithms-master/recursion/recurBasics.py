# a problem can be solved by recursion if loops can solve it. The opposite is same.
# loops vs recursion: loops is faster.
#       calling function takes stack memory in each calls. stack can overflow.
# iterative way (loops)
def print_stars_loop(n: int):
    for i in range(n):
        print("*", end="")

# recursive way (without loops)
def print_stars_recur(n: int):
    # Base case (trivial case: the answer is obvious): stop recursion or can return answer
    if n == 1:
        print("*", end="")
    else:
        # Recursive case: need to call function again
        print("*", end="")
        print_stars_recur(n-1)

print_stars_loop(3)
print()
print_stars_recur(3)
print()

def fatorial_loop(n: int):
    res = 1
    for i in range(2, n+1):  # starts from 2 because 1*1=1, so can be skipped
        res *= i
    return res

def fatorial_recur(n: int):
    if n == 0:
        return 1

    return n * fatorial_recur(n-1)

# factorial(3) = 3! = 3*2*1
# 0! = 1
# 1! = 1
print(fatorial_loop(3))
print(fatorial_recur(3))


def power_loop(base: int, exp: int):
    if base <= 0:
        return 0
    res = 1
    for _ in range(exp):    # "_" means index value is not being used in the loop
        res *= base
    return res

def power_recur(base: int, exp: int):
    if exp <= 0:    # if exp == 0: if exp is < 0, then error will be thrown
        return 1

    return base * power_recur(base, exp-1)

# power(3, 5) = 3*3*3*3*3
# power(3, 0) = 1
base, power = 0, 10
print(f"---------- Power of Base ({base}, {power}) ----------")
print(power_loop(base, power))
print(power_recur(base, power))


# from website
def fibonacci_loop(n: int) -> int:
    # res = [1, 2, 3]
    # for i in range(1, n+1):
    #     if n == 1 or n == 2:
    #         res.append(1)
    #     else:
    #         res.append(res[i-1])
    #
    # return returnes

    a, b = 1, 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(n - 2):
            a, b = b, a + b
        return b

# N-th fibonacci number
# Time Compelexity: O(n)
def fibonacci_loop2(n: int) -> int:
    f, s = 1, 1
    for _ in range(n - 1):
        f, s = s, f + s
    return f

# Time Compelexity: 0(2^n)
def fibonacci_recur(n: int) -> int:
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2)


# fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...
print("fibonacci")
print([fibonacci_loop(n) for n in range(1, 10)])
print(fibonacci_loop2(4))


# N-th Tribonacci Number
# T : 0, 1, 1, (0+1+1)=2, (1+1+((0+1+1))=4, (1+2+4)=7, ...
#   : 0, 1, 1, 2, 4, 7, 13, 24, ...
# if n = 4, return 4
# Time Compelexity: O(n): to improve this, use dynamic programming
def tribonacci_loop(n: int) -> int:
    if n == 0:
        return 0

    f, s, t = 0, 1, 1
    for _ in range(3, n+1):
        f, s, t = s, t, f + s + t
    return t

# Time Compelexity: 0(3^n)
def tribonacci_recur(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recur(n-1) + fibonacci_recur(n-2) + fibonacci_recur(n-3)


print("tribonacci")
print(tribonacci_loop(4))
print(tribonacci_recur(4))
