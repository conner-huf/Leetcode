from typing import List

# url: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

# -------------------------------------------------------------------- #

'''
This solution uses two pointers to iterate through the array of numbers. This solution uses the fact that the array is sorted from lowest number to highest. Because it is sorted, we can start the two pointers at the lowest and highest number and compare the sum of those two numbers to the target. When it is less than the target, we move the left pointer to the right. When it is greater than the target, we move the right pointer to the left. Eventually, we find the two numbers that add up to the target. Because the array is 1-indexed, we add 1 to the indices of the two numbers before returning them.

Time complexity: O(n)
Space complexity: O(1)
'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]