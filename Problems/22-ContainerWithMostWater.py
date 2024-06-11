# url: https://leetcode.com/problems/container-with-most-water/

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea = 0
        
        while l < r:
            currWidth = r - l
            currHeight = min(height[l], height[r])
            
            maxArea = max((currWidth * currHeight), maxArea)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
            
        return maxArea
            