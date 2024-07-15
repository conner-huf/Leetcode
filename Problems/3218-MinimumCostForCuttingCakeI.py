from typing import List

#url: https://leetcode.com/problems/minimum-cost-for-cutting-cake-i/

class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        ROWS = m
        COLS = n

        cuts = [(cost, 0) for cost in horizontalCut] + [(cost, 1) for cost in verticalCut]
        cuts.sort(reverse=True)
        print(cuts)

        total_cost = 0
        horizontal_pieces = 1
        vertical_pieces = 1

        for cost, cut_type in cuts:
            if cut_type == 0:  # Horizontal cut
                total_cost += cost * vertical_pieces
                horizontal_pieces += 1
                print("cut horizontally, now have", horizontal_pieces, "horizontal pieces")
                print("Total cost:", total_cost)
            else:  # Vertical cut
                total_cost += cost * horizontal_pieces
                vertical_pieces += 1
                print("cut vertically, now have", vertical_pieces, "vertical pieces")
                print("Total cost:", total_cost)
        
        return total_cost