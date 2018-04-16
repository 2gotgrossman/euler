def sum_of_multiples(max_num, factors):
    total = 0
    for num in range(1, max_num):
        if any(map(lambda factor: num % factor == 0, factors)):
            total += num
    return total

if __name__ == "__main__":
    print(sum_of_multiples(1000, [3,5]))
