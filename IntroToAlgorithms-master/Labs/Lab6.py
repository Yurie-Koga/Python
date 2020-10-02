""" Primes, GCD, LCM """
import math

def is_prime(n: int):
    """ Check if n is prime """
    if n == 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True



def gcd(a: int, b: int):
    """ GCD of a and b """
    while b != 0:
        (a, b) = (b, a % b)
    return a


def lcm(a: int, b:int):
    """ LCM of a and b """
    return (a * b) / gcd(a, b)



def generate_primes(n: [int]):
    """
    Generating a list of primes

    :return: a list of primes from 2 to n
    """
    # prime_list = []
    # for i in range(2, n):
    #     if is_prime(i) is True:
    #         prime_list.append(i)

    return list(map(lambda x: is_prime(x), n))
