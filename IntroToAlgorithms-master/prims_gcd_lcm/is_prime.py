
import math
import time

def is_prime_base(n: int):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def is_prime_improved(n: int) -> bool:
    if n == 1:
        return False
    #for i in range(2, n // 2):  # this is still half.
    for i in range(2, int(math.sqrt(n)) + 1):   # int(math.sqrt(n)) trim under zero, so add 1
        if n % i == 0:
            return False
    return True

print(math.sqrt(100000))
print(int(math.sqrt(100000)))


def generate_prime_list(n: int, fn):
    """
    Returns a list of primee numbers between 2 and n
    :param n: upper bound
    :return: a list of prime numbers
    """
    prime_list = []
    for i in range(2, n):
        if fn(i) is True:
            prime_list.append(i)
    return prime_list

# n= 100000, took: 33.46 seconds
start_time = time.time()
#generate_prime_list(100000, is_prime_base)  # can pass function
end_time = time.time()
print(f"took: {end_time - start_time} seconds")
# n= 100000, took: 0.19 seconds
start_time = time.time()
#generate_prime_list(100000, is_prime_improved)
end_time = time.time()
print(f"took: {end_time - start_time} seconds")