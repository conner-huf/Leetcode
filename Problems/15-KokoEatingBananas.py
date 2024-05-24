# url: https://leetcode.com/problems/koko-eating-bananas/

# -------------------------------------------------------------------- #

'''
This solution uses a binary search to find the minimum eating speed. We first set the left and right bounds of the binary search to 1 and the maximum pile size, respectively. We then iterate through the piles, calculating the number of hours it would take to eat all the piles at the current speed. If the number of hours is less than or equal to h, we update the right bound of the binary search. Otherwise, we update the left bound. We continue this process until the left bound is less than the right bound. We return the right bound as the minimum eating speed.
'''

from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            m = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            if hours <= h:
                r = min(r, m)
            else:
                l = m + 1
        
        return r
    
    