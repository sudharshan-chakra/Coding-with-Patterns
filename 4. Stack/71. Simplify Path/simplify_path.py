class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for ch in path+"/":
            if ch == "/":
                if cur == "..":
                    if stack: stack.pop()
                elif cur not in ["","."]:
                    stack.append(cur) 
                cur = ""
            else:
                cur += ch

        return "/" + "/".join(stack)