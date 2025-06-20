MAX = 10**12
a, b = map(int, input().split())
if 1 <= b <= a <= MAX:
    odd_count = (a + 1) // 2
    if b <= odd_count:
        print(2 * b - 1)
    else:
        print(2 * (b - odd_count))