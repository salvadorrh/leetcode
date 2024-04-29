"""
Leetcode Problem: 125
Name: Valid Palindrome
https://leetcode.com/problems/valid-palindrome/
"""

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Substitute non letters
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s)
        new_str = new_str.lower() # lowercase
        rev_str = new_str[::-1]

        return new_str == rev_str
        
