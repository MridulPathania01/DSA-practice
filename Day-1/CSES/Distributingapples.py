#Distributing Apples
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     result = 1
#     for i in range(2, n + 1):
#         result *= i
#     return result


MOD= 10**9 + 7
from math import factorial
def apple_distribution(n, m):
    return factorial(m + n - 1) // (factorial(m) * factorial(n - 1))

n,m=map(int,input().split(" ")) #m<10**6
if m < 0 or n <= 0:
    print(0)
else:
    print(apple_distribution(n, m) %MOD)