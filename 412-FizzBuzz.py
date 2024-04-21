"""
Leetcode Problem: 412
Name: Fizz Buzz
https://leetcode.com/problems/fizz-buzz/
"""

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        l = []
        for i in range(1, n+1):
            str_ = ""
            if i % 3 == 0:
                str_ += "Fizz"
            if i % 5 == 0:
                str_ += "Buzz"
            if i % 3 != 0 and i % 5 != 0:
                str_ += str(i)

            l.append(str_)   
            
        return l
        
