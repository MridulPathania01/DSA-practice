def find_two_divisors(a, b):
    for x in range(a, b + 1):
        if x % 2 == 0 and x > 2:
            return (2, x - 2)
    return -1
a, b = map(int, input().split())
print(find_two_divisors(a, b))