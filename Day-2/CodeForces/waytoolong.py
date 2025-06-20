for i in range(int(input())):
    a=input()
    if len(a)<=10:
        print(a)
    else:
       print(a[:1]+str(len(a[1:len(a)-1]))+a[-1])
       