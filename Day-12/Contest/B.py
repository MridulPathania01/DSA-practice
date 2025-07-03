def B():
    n, j, k = map(int, input().split())
    a = list(map(int, input().split()))

    if k > 1:
        print("YES")
    else:
        max_strength = max(a)
        if a[j - 1] == max_strength:
            print("YES")
        else:
            print("NO")


t = int(input())
for _ in range(t):
    B()