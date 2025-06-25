for i in range(int(input())):
    a = input()
    k=0
    for j in range(len(a)):
        if a[j] == '1':
            k += 1
    print(k)