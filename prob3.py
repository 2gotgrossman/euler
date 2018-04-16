from itertools import takewhile
from collections import defaultdict
from typing import Generator, DefaultDict


def primes(upper_limit = None) -> Generator[int, None, None]:
    """
    A generator that yields prime numbers starting with 2
    :return: Generator[int]
    """

    if not upper_limit:
        upper_limit = float('inf')

    primes = [2]
    curr_num = primes[-1]
    while curr_num < upper_limit:
        if all(map(lambda prime_number: curr_num % prime_number != 0, primes)):
            primes.append(curr_num)
            yield curr_num
        curr_num += 1

def prime_factors(num: int) -> DefaultDict[int, int]:
    """
    Returns the prime number factorization of a number
    :param num:
    :return: A dictionary where the key is the prime number and the value is the number of occurrences of the prime number
    """

    factors = defaultdict(int)
    while num > 1:
        for prime in takewhile(lambda p: p <= num, primes()):
            if num % prime == 0:
                num //= prime
                factors[prime] += 1
                break
    return factors

def largest_prime_factor(num: int) -> int:
    return max(prime_factors(num).keys())

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
