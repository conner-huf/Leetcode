# url: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        result = nums[l]
        
        while l <= r:
            if nums[l] < nums[r]:
                result = min(result, nums[l])
                break
            
            m = (l + r) // 2
            
            result = min(result, nums[m])
            
            if nums[l] <= nums[m]:
                l = m + 1
            else:
                r = m - 1
        
        return result