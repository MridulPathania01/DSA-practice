from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l=[]
        a=[]
        for i in range(len(nums)):
             if nums[i]==key:
                a.append(i)
        for i in range(len(nums)):
            for idx in a:
                if abs(i - idx) <= k:
                    l.append(i)
                    break
        print(l)