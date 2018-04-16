from itertools import combinations_with_replacement
# from typing import

def is_palindrome(val: str) -> bool:
    chars = list(str(val))
    for i in range(len(chars) // 2):
        if chars[i] != chars[-1-i]:
            return False
    return True

def find_largest_palindrome(max_num = 999):
    max_palindrome = 0
    for val1, val2 in combinations_with_replacement(range(1, max_num + 1), 2):
        product = val1 * val2
        if is_palindrome(product) and product > max_palindrome:
            max_palindrome = product
    return max_palindrome

if __name__ == "__main__":
    print(find_largest_palindrome())