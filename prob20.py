from _functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1))

print(
    sum(
        map(int, str(factorial(100)))
    )
)
