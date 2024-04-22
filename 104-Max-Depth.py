"""
Leetcode Problem: 104
Name: Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        elif root.left is None:
            return 1 + self.maxDepth(root.right)
        elif root.right is None:
            return 1 + self.maxDepth(root.left)

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        """

        # Better solution
        if root is None:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return 1 + max(left, right)
        
