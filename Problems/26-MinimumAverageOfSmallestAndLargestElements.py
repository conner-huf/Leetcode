'''

from contest:

You have an array of floating point numbers averages which is initially empty. You are given an array nums of n integers where n is even.

You repeat the following procedure n / 2 times:

Remove the smallest element, minElement, and the largest element maxElement, from nums.
Add (minElement + maxElement) / 2 to averages.
Return the minimum element in averages.

'''

from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        
        averages = []
        
        for i in range(len(nums)//2):
            avgToAdd = (min(nums) + max(nums)) / 2
            
            nums.remove(min(nums))
            nums.remove(max(nums))
            
            averages.append(avgToAdd)
            
        return min(averages)