"""
Leetcode Problem: 141
Name: Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Without constant memory requirement:
        # This is easy to solve, simply loop thorugh the linked list
        # and put everything into a set, if we visit an address previously
        # seen then return true, else false.

        """
        # First solution
        seen = set()

        while (head):
            if (head in seen):
                return True
            seen.add(head)
            head = head.next

        return False"""

        tortoise = head # Slow
        hare = head # Fast

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next
            if tortoise == hare:
                return True

        return False
