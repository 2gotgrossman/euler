from _functools import reduce
from typing import Tuple, Iterable

def div_by_all(number: int, factors: Iterable[int]) -> bool:
    """
    Returns whether `number` is divisible by each and every element of `factors`
    """
    return all(map(lambda factor: number % factor == 0, factors))


def smallest_number_div_by_all(factors: Iterable[int]) -> int:
    """
    returns the smallest number that is divisible by every number in `factors`
    """
    product = reduce(lambda x, y: x * y, factors)
    for factor in reversed(factors):
        if product % factor == 0 and div_by_all(product // factor, factors):
            product //= factor
    return product

if __name__ == "__main__":
    print(smallest_number_div_by_all(range(1, 21)))