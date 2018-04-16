from typing import Iterable

def sum_of_squares(nums: Iterable[int]) -> int:
    return sum(map(lambda x: x ** 2, nums))

def square_of_sums(nums: Iterable[int]) -> int:
    return sum(nums) ** 2

def sum_square_diff(nums: Iterable[int]) -> int:
    return square_of_sums(nums) - sum_of_squares(nums)

if __name__ == "__main__":
    print(sum_square_diff(range(1, 101)))