"""
Leetcode Problem: 118
Name: Pascal's Triangle
https://leetcode.com/problems/pascals-triangle/
"""

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pt = [[1]] # Pascal Triangle values
        for r in range(1, numRows):
            newRow = [0]*(r+1) 
            newRow[0] = 1
            newRow[-1] = 1
            lastRow = pt[r-1]
            print(lastRow)
            for i in range(1,r):
                newRow[i] = lastRow[i-1] + lastRow[i]
            pt.append(newRow)

        return pt
        
