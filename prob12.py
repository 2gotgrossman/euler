from math import sqrt

def get_divisors(number):
    """
    return a list of the divisors of a number
    :param number:
    :return:
    """
    divisors = set()

    for i in range(1, int(sqrt(number)) + 1):
        if number % i == 0:
            divisors.add(i)
            divisors.add(number // i)
    return divisors

def triangular_numbers():
    i = 0
    total = 0
    while True:
        i += 1
        total += i
        yield total

def first_number_with_over_n_divisors(n):
    for i in triangular_numbers():
        if len(get_divisors(i)) > n:
            return i

if __name__ == "__main__":
    print(first_number_with_over_n_divisors(500))