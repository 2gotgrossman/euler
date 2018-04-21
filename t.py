from typing import Generator

def primes(upper_limit = None) -> Generator[int, None, None]:
    """
    A generator that yields prime numbers starting with 2
    :upper_limit: Optional parameter for a maximum prime number to yield
    :return: Generator[int, None, None]
    """

    if not upper_limit:
        upper_limit = float('inf')

    primes = []
    current = 2
    while current < upper_limit:
        # Lazily evaluates divisibility
        divisible_by_primes = map(lambda prime: current % prime == 0, primes)
        if not any(divisible_by_primes):
            primes.append(current)
            yield current
        current += 1


ps = primes()
for i, p in zip(range(5), ps):
    print(p)
