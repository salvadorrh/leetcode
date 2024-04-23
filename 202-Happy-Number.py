"""
Leetcode Problem: 202
Name: Happy Number
https://leetcode.com/problems/happy-number/
"""

class Solution:
    def isHappy(self, n: int) -> bool:
        seenDigits = set()
        while True:
            n = self.squareDigits(n)
            if n == 1:
                return True
            if n in seenDigits:
                return False
            seenDigits.add(n)


        return False

    def squareDigits(self, n: int) -> int:
        sumSquares = 0
        while n > 0:
            digit = n % 10
            sumSquares += digit ** 2
            n //= 10 # To get rid of the last digit
        
        return sumSquares
        
