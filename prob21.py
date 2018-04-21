from prob12 import get_divisors

nums_to_divisors = {i : get_divisors(i) - set([i]) for i in range(1, 10001)}
nums_to_sum_of_divisors = {k : sum(v) for k, v in nums_to_divisors.items()}

amicables = set()
for a in range(1, 10001):
    b = nums_to_sum_of_divisors[a]
    d_b = nums_to_sum_of_divisors.get(b, -1)

    if a != b and a == d_b:
        amicables.add(a)

print(sum(amicables))