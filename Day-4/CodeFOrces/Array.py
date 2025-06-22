from math import factorial
MOD= 10**9 + 7
def modinv(x):
    return pow(x, MOD - 2, MOD)
def rabbit(n,k):
    numerator = factorial(n) % MOD
    denominator = (factorial(k) * factorial(n - k)) % MOD
    return numerator * modinv(denominator) % MOD
def co(n):
    t=rabbit(2*n-1,n)
    r=(2*t-n)%MOD
    return r
n=int(input())
print(co(n))