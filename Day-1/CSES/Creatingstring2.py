MOD = 10**9 + 7
MAX = 10**6 + 10
fact = [1] * MAX
inv_fact = [1] * MAX
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD
inv_fact[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
for i in range(MAX - 2, 0, -1):
    inv_fact[i] = inv_fact[i + 1] * (i + 1) % MOD

from collections import Counter
def distinct_permutations_mod(s):
    freq = Counter(s)
    n = len(s)
    res = fact[n]
    for count in freq.values():
        res = res * inv_fact[count] % MOD
    return res
a=input()
print(distinct_permutations_mod(a))
