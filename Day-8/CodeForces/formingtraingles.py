#forming triangles
from typing import List
class Solution:
    def formingTriangles(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0
        for i in range(n - 1, 1, -1):
            left, right = 0, i - 1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1
        return count
if __name__ == "__main__":
    for i in range(int(input())):
        n = int(input())
        nums = list(map(int, input().split()))
        
        solution = Solution()
        print(solution.formingTriangles(nums))
        