T = int(input())
for _ in range(T):
    n = int(input())
    a = list(map(int, input().split()))
    pref_min = [0] * n
    suff_max = [0] * n

    pref_min[0] = a[0]
    for i in range(1, n):
        pref_min[i] = min(pref_min[i - 1], a[i])

    suff_max[n - 1] = a[n - 1]
    for i in range(n - 2, -1, -1):
        suff_max[i] = max(suff_max[i + 1], a[i])
    ans = ['0'] * n
    for i in range(n):
        if a[i] == pref_min[i] or a[i] == suff_max[i]:
            ans[i] = '1'

    print(''.join(ans))