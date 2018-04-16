"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from prob3 import primes
from itertools import takewhile






def sieve(max_prime = 2000000):
    def next_prime(curr_number):
        while True:
            curr_number += 1
            if curr_number not in visited:
                return curr_number

    def add_new_primes(curr_number):
        for i in range(curr_number, max_prime + 1, curr_number):
            visited.add(i)


    visited = set()
    curr_prime = 2
    add_new_primes(curr_prime)

    while curr_prime < max_prime:
        yield curr_prime
        curr_prime = next_prime(curr_prime)

        add_new_primes(curr_prime)




def sum_of_primes(max_prime_value = 2000000, debug=False) -> int:
    total = 0
    for i, p in enumerate(sieve(max_prime_value)):
        total += p
        if debug and (i < 20 or i % 10000 == 0):
            print(i, p, total)
    return total

print(sum_of_primes(max_prime_value=20000000, debug=True))
