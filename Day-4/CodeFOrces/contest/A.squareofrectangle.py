from itertools import permutations
def can_form_square(l1, b1, l2, b2, l3, b3):
    rects = [(l1, b1), (l2, b2), (l3, b3)]
    total_area = l1*b1 + l2*b2 + l3*b3
    from math import isqrt
    S = isqrt(total_area)
    if S * S != total_area:
        return False
    for (a1, b1), (a2, b2), (a3, b3) in permutations(rects):
        if b1 + max(b2, b3) == S and a1 == S and a2 + a3 == S and max(b2, b3) <= S:
            return True

        if a1 + max(a2, a3) == S and b1 == S and b2 + b3 == S and max(a2, a3) <= S:
            return True
        if b1 == b2 == b3 and b1 == S and a1 + a2 + a3 == S:
            return True
        if a1 == a2 == a3 and a1 == S and b1 + b2 + b3 == S:
            return True
    return False
t = int(input())
for _ in range(t):
    l1, b1, l2, b2, l3, b3 = map(int, input().split())
    print("YES" if can_form_square(l1, b1, l2, b2, l3, b3) else "NO")
