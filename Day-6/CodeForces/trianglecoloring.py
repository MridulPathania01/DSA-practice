import sys
from math import gcd
from collections import defaultdict
from itertools import combinations

MOD = 998244353
MAX = int(2e5 + 7)
def input():
    return sys.stdin.readline()
fact = [1] * MAX

def pre_factorial():
    for i in range(1, MAX):
        fact[i] = (fact[i - 1] * i) % MOD

def binpowmod(a, b, mod=MOD):
    result = 1
    a %= mod
    while b > 0:
        if b & 1:
            result = (result * a) % mod
        a = (a * a) % mod
        b >>= 1
    return result

def modinv(a):
    return binpowmod(a, MOD - 2)

def divide(a, b):
    return (a * modinv(b)) % MOD

def nCr(n, r):
    if n < r:
        return 0
    return divide(fact[n], (fact[r] * fact[n - r]) % MOD)

def solve():
    n = int(input())
    groups = []
    for _ in range(n // 3):
        arr = list(map(int, input().split()))
        arr.sort()
        groups.append(arr)

    ans = nCr(n // 3, n // 6)

    for arr in groups:
        if arr[0] == arr[1] == arr[2]:
            ans = (ans * 3) % MOD
        elif arr[0] == arr[1]:
            ans = (ans * 2) % MOD

    print(ans)
if __name__ == "__main__":
    pre_factorial()
    solve()