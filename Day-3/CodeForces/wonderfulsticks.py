def test():
    n = int(input())
    s = input().strip()
    l = 1
    r = n
    a = [0] * n
    for i in range(n - 2, -1, -1):
        if s[i] == '<':
            a[i + 1] = l
            l += 1
        if s[i] == '>':
            a[i + 1] = r
            r -= 1
    a[0] = l
    print(' '.join(map(str, a)))
t = int(input())
for _ in range(t):
    test()