# s=int(input())
# b=[]
# a=list(map(int, input().split(" ")))
# for i in range(len(a)):
#     for j in range(i+1, len(a)):
#         b.append(abs(a[i]-a[j]))
# l=max(b)
# w=b.count(l)
# print(l,w)

# optmised
from typing import List
class Solution:
    def pashmakAndFlowers(self, flowers: List[int]) -> List[int]:
        min_flower = min(flowers)
        max_flower = max(flowers)
        count_min = flowers.count(min_flower)
        count_max = flowers.count(max_flower)
        
        if min_flower == max_flower:
            return [0, count_min * (count_min - 1) // 2]
        else:
            return [max_flower - min_flower, count_min * count_max]
if __name__ == "__main__":
    s = int(input())
    flowers = list(map(int, input().split()))
    
    solution = Solution()
    result = solution.pashmakAndFlowers(flowers)
    print(result[0], result[1])