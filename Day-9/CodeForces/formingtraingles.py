from collections import Counter

def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        v = list(map(int, input().split()))
        f = Counter(v)
        ans = 0
        tot = 0
        for key in sorted(f):
            x = f[key]
            if x > 1:
                if x > 2:
                    ans += x * (x - 1) * (x - 2) // 6
                    ans += x * (x - 1) // 2 * tot
                    tot += x
                else:
                    tot += x
                    ans += tot - x
            else:
                tot += x
        print(ans)

if __name__ == "__main__":
    solve()