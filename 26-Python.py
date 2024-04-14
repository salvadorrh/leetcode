"""
Leetcode Problem: 26
Name: Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Have two pointers
        - Pointer 1 with current number to place
        - Pointer 2 where to place it
        """
        ptr1 = 0
        prevValue = nums[0]-1
        uniques = 0

        for ptr2 in range(len(nums)):
            if nums[ptr2] != prevValue:
                nums[ptr1] = nums[ptr2]
                prevValue = nums[ptr2]
                ptr1 += 1
                uniques += 1
        
        return uniques


        
