# url: https://leetcode.com/problems/longest-consecutive-sequence/

'''
This solution is based on the idea that we can find the longest consecutive sequence by iterating through the numbers and checking if the number - 1 is in the set. If it is not, then we know that this number is the start of a new sequence. We then iterate through the numbers in the sequence and keep track of the length of the sequence. We update the longest sequence length whenever we find a longer sequence.
'''

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in numSet:
                length = 0
                while (num + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest