def solve():
    n, s = map(int, input().split())
    res = 0
    for _ in range(n):
        dx, dy, xi, yi = map(int, input().split())
        if dx == dy:
            if (xi - yi) % s == 0:
                res += 1
        else:
            if (xi + yi) % s == 0:
                res += 1
    print(res)

def main():
    t = int(input())
    for _ in range(t):
        solve()
if __name__ == "__main__":
    main()