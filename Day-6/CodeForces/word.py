a=input()
b,c=0,0
for i in range(len(a)):
    if a[i].isupper():
        b+=1 
    elif a[i].islower():
        c+=1
if b>c:
    print(a.upper())
elif c>b:
    print(a.lower())
else:
    print(a.lower())