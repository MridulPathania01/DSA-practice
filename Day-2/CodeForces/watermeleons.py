#Watermelons codeforces problem solution
def can_divide_watermelons(n):
    if n % 2 == 0 and n > 2:
        return "YES"
    else:
        return "NO"
n = int(input())
print(can_divide_watermelons(n))
