from prob3 import primes
from itertools import islice

take = lambda n, iterable: list(islice(iterable, n-1))

print(take(10001, primes())[-1])