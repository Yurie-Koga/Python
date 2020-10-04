"""
Lab6 is also Prime/GCD/LCM
"""


import math
import time

def is_prime_base(n: int):
    pass
def is_prime_improved(n: int) -> bool:
    pass


def gcd(a: int, b: int):
    pass


def lcm(a: int, b:int):
    """ LCM of a and b """
    pass

def generate_prime_list(n: int, fn):
    """
    Returns a list of primee numbers between 2 and n
    :param n: upper bound
    :return: a list of prime numbers
    """
    pass


if __name__== '__main__':
    print(math.sqrt(100000))
    print(int(math.sqrt(100000)))


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