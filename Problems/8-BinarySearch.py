# url: https://leetcode.com/problems/binary-search/

# -------------------------------------------------------------------- #

'''
    This solution uses a binary search algorithm (as the name of the problem would suggest) to find the target in the nums array. 

    This algorithm is super valuable to understand because it is 1) very common and 2) very efficient. Binary search works with sorted arrays, and finds the target in O(log n) time. With binary search, you use the fact that the array is sorted start with looking at the whole of the array. You compare the middle element to the target and if it is greater than the target, you know the target would be before that middle element if it exists. If the middle element is less than the target, you know the target would be after that middle element if it exists. This way, you eliminate half of the array each time you iterate.

    Time complexity: O(log n)
    Space complexity: O(1)
'''

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            elif nums[m] == target:
                return m
        
        return -1