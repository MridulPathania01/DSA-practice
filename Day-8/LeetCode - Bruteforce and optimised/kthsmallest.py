from typing import List
# brute force
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        a=[]
        b=len(nums1)
        c=len(nums2)
        for i in range(b):
            for j in range(c):
                a.append(nums1[i]*nums2[j])
        a.sort()
        return a[k-1]
    
# optimised last wrong
import bisect
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def countLessEqual(x):
            count = 0
            for num in nums1:
                if num > 0:
                    count += bisect.bisect_right(nums2, x // num)
                elif num < 0:
                    count += len(nums2) - bisect.bisect_left(nums2, (x + 1) // num)
                else:
                    if x >= 0:
                        count += len(nums2)
            return count

        left, right = -10**10, 10**10
        while left < right:
            mid = (left + right) // 2
            if countLessEqual(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left