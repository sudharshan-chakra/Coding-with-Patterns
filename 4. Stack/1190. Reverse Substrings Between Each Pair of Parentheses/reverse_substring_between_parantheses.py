class Solution:
    def reverseParentheses(self, s: str) -> str:
        '''
        The time complexity of this solution is O(N * M) where
            - N is the size of the input string and 
            - M is the number of pairs of parentheses

        The space complexity is O(N) 
        '''
        stack = []

        for ch in s:
            if ch == ")":
                temp = []
                while stack[-1] != "(":
                    temp.append(stack.pop())
                stack.pop()    # remove opening "("
                for t in temp:
                    stack.append(t)
            else:
                stack.append(ch)

        return "".join(stack)