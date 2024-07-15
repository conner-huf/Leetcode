# url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# -------------------------------------------------------------------- #

'''
This solution uses a two-pointer approach to iterate through the input list. We keep track of the maximum profit we can make by buying at the left pointer and selling at the right pointer. If the price at the right pointer is greater than the price at the left pointer, we calculate the profit and update the maximum profit if necessary. If the price at the right pointer is less than the price at the left pointer, we update the left pointer to the right pointer. We continue this process until we reach the end of the input list.
'''

from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1
        
        return maxP