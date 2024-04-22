"""
Leetcode Problem: 70
Name: Climbing stairs
https://leetcode.com/problems/climbing-stairs/
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        P(n) -> Number of possible ways to climb to the top
        P(n) = P(n-1) + P(n-2)
        -Since from the n-1th step you can simply reach to the top by taking one more step
        -And from the n-2th step you can simply reach to the top by taking a climb of two steps
        """
        # Error time limit solution:
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        """

        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        ps = [0] * (n+1)
        ps[1] = 1
        ps[2] = 2

        for i in range(3, n+1):
            ps[i] = ps[i-1] + ps[i-2]

        return ps[n]
