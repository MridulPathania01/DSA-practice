#Christmas Party
from math import factorial
def chritmasparty(n):
    return (factorial(n)//n)%MOD

MOD= 10**9 + 7
n=int(input())
print(chritmasparty(n))
