for _ in range(int(input())):
    a,x,y=map(int,input().split())
    if (a<x)==(a<y):
        print("yes")
    else:
        print("no")