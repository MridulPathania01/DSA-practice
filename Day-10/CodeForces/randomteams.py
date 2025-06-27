n,m=map(int,input().split())
a= (n - m + 1) * (n - m) // 2
b= (m - n % m) * (n // m) * (n // m - 1) // 2 + (n % m) * (n // m + 1) * (n // m) // 2
print(b,a)