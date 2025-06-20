def solve():
    n = int(input())
    print(2 * n - 1)
    print(1, 1, n)
    for i in range(2, n + 1):
        print(i, 1, i - 1)
        print(i, i, n)

T = int(input())
for _ in range(T):
    solve()
