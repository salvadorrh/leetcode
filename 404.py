"""
Leetcode Problem: 404
Name: Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/description/?envType=daily-question&envId=2024-04-14
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0

        val = 0
        if root.left != None:
            if root.left.left == None and root.left.right == None:
                val = root.left.val
        
        return val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
