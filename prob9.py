from math import sqrt

for a in range(1, 1000):
    for b in range(a+1, 1000):
        c = sqrt(a**2 + b**2)
        c_is_int = c == int(c)
        c_greater_than_a_and_b = c > b > a
        sum_is_1000 = a + b + c == 1000

        if c_is_int and c_greater_than_a_and_b and sum_is_1000:
            print((a,b,int(c)), a * b * int(c))

