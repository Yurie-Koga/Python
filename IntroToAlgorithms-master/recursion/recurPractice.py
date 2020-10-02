"""
Recursion vs Loops practice.
Copy and paste repeatedly to practice a lot.
"""

"""
Return strings with the length of n
"""
def print_stars_loop(n: int) -> str:
    s = ""
    for i in range(n):
        s += "*"
    return s

def print_stars_recur(n: int) -> str:
    if n <= 0:
        return ""

    return "*" + print_stars_recur(n-1)


"""
Return a factorial
Factorial
0! = 1
1! = 1
2! = 2*1
3! = 3*2*1
"""
def factorial_loop(n: int) -> int:
    res = 1
    for i in range(2, n+1):
        res *= i
    return res

def factorial_recur(n: int) -> int:
    if n <= 1:
        return 1

    return n * factorial_recur(n-1)


"""
Return a power of base
3^5 = 3*3*3*3*3
base^power = base*base*base*..
0^1 = 0
3^0 = 1
3^1 = 3
3^2 = 9
"""
def power_loop(base: int, power: int) -> int:
    # did not consider negative
    if base == 0:
        return 0
    if base == 1 or power <= 0:
        return 1

    # res = 1
    # for _ in range(power):
    #     res *= base
    res = base
    for i in range(1, power):
        print(f"index: {i}")
        res *= base
    return res

def power_recur(base: int, power) -> int:
    if base == 0:
        return 0
    if base == 1 or power <= 0:
        return 1

    return base * power_recur(base, power-1)



"""
Return a fibonacci number from 1 to N-th
fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
"""
def fibonacci_seq_loop(n: int) -> [int]:
    # f0, f1 = 0, 1
    # if n == 0:
    #     return f0
    # elif n == 1:
    #     return f1
    #
    # for i in range(2, n):
    #     f0, f1 = f1, f0 + f1
    # return f0
    pass

def fibonacci_seq_recur(n: int) -> [int]:

    pass


"""
Return the N-th Fibonacci number
fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
0th = 0
4th = 3
7th = 13
"""
def fibonacci_nth_start0_loop(n: int) -> int:
    f0, f1 = 0, 1
    # if n == 0:    # it's obvious to write here, but range in python can ignore this case.
    #     return f0
    # elif n == 1:
    #     return f1
    #
    # for i in range(1, n+1):
    #     f0, f1 = f1, f0 + f1
    #     print(f"index: {i}, f0: {f0}, f1: {f1}")

    for i in range(n):  # range(0) = 0 <= < 0 -> when n = 0 then loop will not run
        f0, f1 = f1, f0 + f1
        # print(f"index: {i}, f0: {f0}, f1: {f1}")
    return f0


def fibonacci_nth_recur(n: int) -> int:
    f0, f1 = 0, 1
    if n == 0:
        return f0
    elif n == 1:
        return f1

    return fibonacci_nth_recur(n-2) + fibonacci_nth_recur(n-1)



"""
Return the N-th Fibonacci number
fibonacci sequence: 1, 1, 2, 3, 5, 8, 13, 21, ...
1th = 1
4th = 3
7th = 13
"""
def fibonacci_nth_start1_loop(n: int) -> int:
    f0, f1 = 1, 1
    # if n == 0:
    #     return f0
    # elif n == 1:
    #     return f1
    #
    # for i in range(1, n+1):
    #     f0, f1 = f1, f0 + f1
    #     print(f"index: {i}, f0: {f0}, f1: {f1}")

    # for i in range(n - 1):
    #     f0, f1 = f1, f0 + f1
    #     print(f"index: {i}, f0: {f0}, f1: {f1}")
    # return f0

    f = 1
    s = 1
    for _ in range(n - 1):  #this does not consider when n=0th. wrong.
        f, s = s, f + s
    return f


"""
Return the N-th Tribonacci Number
T : 0, 1, 1, (0+1+1)=2, (1+1+((0+1+1))=4, (1+2+4)=7, ...
  : 0, 1, 1, 2, 4, 7, 13, 24, ...
0th = 0
4th = 4
7th = 24
"""
def tribonacci_nth_loop(n: int) -> int:
    t0, t1, t2 = 0, 1, 1
    for _ in range(n):
        t0, t1, t2 = t1, t2, t0 + t1 + t2
    return t0

def tribonacci_nth_recur(n: int) -> int:
    t0, t1, t2 = 0, 1, 1
    if n == 0:
        return t0
    elif n == 1:
        return t1
    elif n == 2:
        return t2

    return tribonacci_nth_recur(n-3) + tribonacci_nth_recur(n-2) + tribonacci_nth_recur(n-1)


if __name__ == "__main__":
    n = 3
    print(f"---------- Print Stars ({n}) ----------")
    print(f"loop : {print_stars_loop(n)}")
    print(f"recur: {print_stars_recur(n)}")

    n = 4
    print(f"---------- Factorial ({n}) ----------")
    print(f"loop : {factorial_loop(n)}")
    print(f"recur: {factorial_recur(n)}")

    base, power = 3, 3
    print(f"---------- Power of Base ({base}, {power}) ----------")
    print(f"loop : {power_loop(base, power)}")
    print(f"recur: {power_recur(base, power)}")

    # n = 3
    # print(f"---------- Fibonacci Sequence ({n}) ----------")
    # print(f"loop : {fibonacci_seq_loop(n)}")
    # print(f"recur: {fibonacci_seq_recur(n)}")

    n = 7
    print(f"---------- Fibonacci N-th number start 0 ({n}) ----------")
    print(f"loop : {fibonacci_nth_start0_loop(n)}")
    print(f"recur: {fibonacci_nth_recur(n)}")

    # n = 0
    # print(f"---------- Fibonacci N-th number start 1 ({n}) ----------")
    # print(f"loop : {fibonacci_nth_start1_loop(n)}")
    # print(f"recur: {fibonacci_nth_recur(n)}")

    n = 7
    print(f"---------- Tribonacci N-th number ({n}) ----------")
    print(f"loop : {tribonacci_nth_loop(n)}")
    print(f"recur: {tribonacci_nth_recur(n)}")