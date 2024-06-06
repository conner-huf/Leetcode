# url: https://leetcode.com/problems/product-of-array-except-self/

'''
This solution is based on the idea that we can find the product of all the numbers in the array except for the current number by keeping track of the prefix and postfix products. We can iterate through the array once to find the prefix products and then iterate through the array again to find the postfix products. We can then multiply the prefix and postfix products to get the final result.
'''

from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result
