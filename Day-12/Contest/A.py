def A():
    n = int(input())
    if n % 4 == 0:
        print("Bob")
    else:
        print("Alice")
t = int(input())
for _ in range(t):
    A()