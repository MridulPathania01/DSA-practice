for i in range(int(input())):
    a = input()
    idx = a.rfind('us')
    if idx != -1:
        a = a[:idx] + 'i' + a[idx+2:]
    print(a)