#Brute Force
# for i in range(int(input())):
#     n,x,y=map(int,input().split())
#     a=list(map(int,input().split()))
#     c=0
#     for i in range(n):
#         for j in range(i+1,n):
#             if (a[i]+a[j])%x==0 and (abs(a[i]-a[j]))%y==0:
#                 c+=1
#     print(c)


# Optimized Approach
from collections import defaultdict
for _ in range(int(input())):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0
    freq = defaultdict(int)
    for num in a:
        key = ((-num) % x, num % y)
        count += freq[key]
        freq[(num % x, num % y)] += 1
    print(count)