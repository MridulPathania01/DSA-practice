for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    
    k = 0
    i = 0
    while i < len(b) - 1:
        if b[i] == b[i + 1]:
            print("0")
            break
        elif b[i] > b[i + 1]:
            diff = b[i] - b[i + 1]
            b.pop(i + 1)
            b[i] = diff
            k += 1
        else:
            i += 1
    else:
        print(k)
                