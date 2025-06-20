# shrink codeforces problem solution
t = int(input())
for _ in range(t):
    s = int(input())
    b=[]*s
    for i in range(1,s+1):
        b.append(i)
    for i in range(1,s-1):
        if b[i] >b[i-1] and b[i]<b[i+1]:
            b[i],b[i+1]=b[i+1],b[i]
            
    print(b)
    
