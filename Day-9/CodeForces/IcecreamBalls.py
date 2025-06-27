a=int(input())
c=0
for i in range(a):
    
    n,x,y=map(int,input().split())
    l=list(map(int,input().split()))
    for j in range(n):
        for k in range(j+1,n):
            if (l[j] + l[k]) % x == 0 and (l[j] - l[k]) % y == 0:
                c += 1
    print(c)         
        