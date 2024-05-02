from typing import List

# url: https://leetcode.com/problems/two-sum/

'''
In this solution, we are given an array of integers and a target value. There is always a solution in the array of integers and there is always exactly one solution. We need to return the indices of the two numbers that add up to the target value. The thought is that we have to remember both an integer and its index, and we have to reference the integers belonging to indices. So we'll consistently need to access integers and we'll need to access two indices at the end of the problem to return the actual solution. This lends itself perfectly to a dictionary, where we're storing keys (integers) and their values (the index of that integer). So we iterate through the array of nums and for each element, we check if the corresponding integer that would add up to the target already exists in the dictionary. If it does we return the values of the key in the dictionary (which would be the lower index) and the index that we are currently on. If it doesn't exist in the dictionary, then we add that element into the dictionary and continue iterating.

Time Complexity: O(n)
Space Complexity: O(n)
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i in range(len(nums)):
            if target - nums[i] in numsDict:
                return [numsDict[target - nums[i]], i]
            else:
                numsDict[nums[i]] = i
        