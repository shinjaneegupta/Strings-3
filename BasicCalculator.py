# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
# Approach : So we go through the expression and compute numbers based on the last operator while pushing intermediate results onto a stack.
# When we hit an open parenthesis, we store the context including signs or operations, and on close parenthesis, we evaluate the entire sub-expression.
# It handles precedence and parentheses, covering Basic Calculator (I) and Basic Calculator III logic together.

class Solution:
    def calculate(self, s: str) -> int:
        st = []
        curNum = 0
        openBrace = float('inf')
        lastSign = '+'
        result = 0
        s = s.strip()

        for i in range(len(s)):
            c = s[i]
            if c.isdigit():
                curNum = curNum * 10 + int(c)
                if i == len(s) - 1:
                    if lastSign == '+':
                        st.append(curNum)
                    elif lastSign == '-':
                        st.append(-curNum)
                    elif lastSign == '*':
                        st.append(st.pop() * curNum)
                    else:
                        st.append(int(st.pop() / curNum))
            elif c == '(':
                if lastSign == '+':
                    st.append(1)
                elif lastSign == '-':
                    st.append(-1)
                elif lastSign == '*':
                    st.append(None)
                elif lastSign == '/':
                    st.append(-float('inf'))
                st.append(openBrace)
                lastSign = '+'
                curNum = 0
            elif c == ')':
                if lastSign == '+':
                    st.append(curNum)
                elif lastSign == '-':
                    st.append(-curNum)
                elif lastSign == '*':
                    st.append(st.pop() * curNum)
                elif lastSign == '/':
                    st.append(int(st.pop() / curNum))
                intrMed = 0
                while st[-1] != openBrace:
                    intrMed += st.pop()
                st.pop()
                if st[-1] is None:
                    st.pop()
                    st.append(st.pop() * intrMed)
                elif st[-1] == -float('inf'):
                    st.pop()
                    st.append(int(st.pop() / intrMed))
                else:
                    st.append(intrMed * st.pop())
                lastSign = ' '
                curNum = 0
            elif c in '+-*/':
                if lastSign == '+':
                    st.append(curNum)
                elif lastSign == '-':
                    st.append(-curNum)
                elif lastSign == '*':
                    st.append(st.pop() * curNum)
                elif lastSign == '/':
                    st.append(int(st.pop() / curNum))
                lastSign = c
                curNum = 0

        while st:
            result += st.pop()
        return result