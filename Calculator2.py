# Time Complexity : O(n)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : We are reading the string left to right and forming numbers digit by digit.
# When we hit an operator, we apply the previous sign and adjust the result based on precedence using a tail tracker.
# This lets us handle * and / immediately without a stack, by reversing the last number and applying the new operation.

class Solution:
    def calculate(self, s: str) -> int:
        currNum = 0
        lastSign = '+'

        calc, tail = 0, 0

        for i in range(len(s)):
            c = s[i]

            if c.isdigit():
                currNum = currNum * 10 + int(c)

            if (not c.isdigit() and c != ' ') or i == len(s) - 1:
                if lastSign == '+':
                    calc = calc + currNum
                    tail = currNum
                elif lastSign == '-':
                    calc = calc - currNum
                    tail = -currNum
                elif lastSign == '*':
                    calc = (calc - tail) + (tail * currNum)
                    tail = tail * currNum
                elif lastSign == '/':
                    calc = (calc - tail) + int(tail / currNum)
                    tail = int(tail / currNum)

                currNum = 0
                lastSign = c

        return calc


            

