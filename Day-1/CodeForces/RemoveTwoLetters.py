#Remove two letters

def solve():
    T = int(input())
    for _ in range(T):
        n = int(input())
        s = input()
        ans = 0
        i = 0
        while i <= n - 2:
            if i == n - 2:
                ans += 1
                break
            if s[i] == s[i + 2]:
                i += 1
            else:
                ans += 1
                i += 1
        print(ans)
solve()