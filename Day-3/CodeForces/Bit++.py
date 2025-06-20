b = 0
for i in range(int(input())):
    a = input()
    if a == "++X" or a == "X++":
        b += 1
    if a == "--X" or a == "X--":
        b -= 1
print(b)