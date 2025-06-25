#optmised approach
# Time Complexity: O(n)
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        a=0
        b=0
        c={0:1}
        for num in nums:
            b+=num
            a+=c.get(b-k,0)
            c[b]=c.get(b,0)+1
        return a

# Brute Force Approach
# Time Complexity: O(n^2)    
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = []
        w=[]
        n=len(nums)
        for i in range(n):
            for j in range(i + 1, n + 1):
                res.append(nums[i:j])
        for i in res:
            if sum(i)==k:
                w.append(i)
        return len(w)    