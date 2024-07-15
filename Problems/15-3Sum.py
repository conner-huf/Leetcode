# url: https://leetcode.com/problems/3sum/

# -------------------------------------------------------------------- #

'''
This solution uses a two-pointer approach to find all the unique triplets that sum to zero. We first sort the input list. We then iterate through the list, using the current value as the first value in the triplet. We then use two pointers to find the other two values in the triplet. We skip over duplicate values to avoid duplicate triplets. If the sum of the three values is greater than zero, we decrement the right pointer. If the sum is less than zero, we increment the left pointer. If the sum is zero, we add the triplet to the result list. We then increment the left pointer and skip over duplicate values. We continue this process until the left pointer is greater than the right pointer.
'''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                elif threeSum == 0:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return result