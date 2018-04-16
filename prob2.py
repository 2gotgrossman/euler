def fibs(max_fib_value = None):
    fib1 = 1
    fib2 = 1

    if not max_fib_value:
        max_fib_value = float('inf')

    while fib2 < max_fib_value:
        yield fib2
        fib1, fib2 = fib2, fib1 + fib2


def get_sum_of_even_fibs():
    total = 0
    for i, fib in enumerate(fibs(max_fib_value=10000000)):
        print(i, fib)
        if (i+1) % 2 == 1:
            print(total)
            total += fib
    return total

if __name__ == "__main__":
    print(get_sum_of_even_fibs())