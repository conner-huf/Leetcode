# url: https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

'''

from contest:

You are given a 2D binary array grid. Find a rectangle with horizontal and vertical sides with the smallest area, such that all the 1's in grid lie inside this rectangle.

Return the minimum possible area of the rectangle.

'''

from typing import List

class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:

        if not grid or not grid[0]:
            return 0

        rows = len(grid)
        cols = len(grid[0])

        top = rows  
        bottom = -1  
        left = cols  
        right = -1  

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    top = min(top, i)
                    bottom = max(bottom, i)
                    left = min(left, j)
                    right = max(right, j)

        width = right - left + 1
        height = bottom - top + 1

        area = width * height

        return area