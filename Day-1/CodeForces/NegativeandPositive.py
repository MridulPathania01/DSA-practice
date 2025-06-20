for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(abs(x) for x in a)
    if sum(x < 0 for x in a) % 2:
        total -= 2 * min(abs(x) for x in a)
    print(total)