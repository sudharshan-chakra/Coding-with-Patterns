class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        fres = []
        count = 0

        for ch in s:
            if ch not in '()':
                fres.append(ch)
            elif ch == "(":
                count += 1
                fres.append(ch)
            else:
                count -= 1
                if count < 0:
                    count += 1
                else:
                    fres.append(ch)
        
        res = []
        for ch in reversed(fres):
            if ch == "(" and count > 0:
                count -= 1
            else:
                res.append(ch)

        return "".join(reversed(res))
