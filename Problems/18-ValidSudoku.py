#url: https://leetcode.com/problems/valid-sudoku/

'''
This solution is based on the idea that we can iterate through the board and keep track of the numbers we have seen in each row, column, and 3x3 square. We can use a set to keep track of the numbers we have seen in each row, column, and square. If we see a number that is already in the set, then we know that the board is not valid. If we make it through the entire board without finding any duplicates, then we know that the board is valid.
'''

from typing import List
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set) # key = (row // 3, col // 3)

        for r in range(9):
            for c in range(9):
                subRow = r // 3
                subCol = c // 3
                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(subRow, subCol)]
                    ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(subRow, subCol)].add(board[r][c])
        
        return True
                
