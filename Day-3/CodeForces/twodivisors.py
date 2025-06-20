import math

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    n = a + b
    divisors = set()
    for i in range(1, int(math.isqrt(n)) + 1):
        if n % i == 0:
            if i < n:
                divisors.add(i)
            if n // i < n:
                divisors.add(n // i)
    largest = sorted(divisors)[-2:]
    print(largest[0] * largest[1])