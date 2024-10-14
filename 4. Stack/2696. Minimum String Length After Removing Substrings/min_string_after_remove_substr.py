class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for i, ch in enumerate(s):
            if not stack:
                stack.append(ch)
                continue

            if stack[-1] + ch in ["AB", "CD"]:
                stack.pop()
            else:
                stack.append(ch)
        
        return len(stack)