class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        jump = 2 * numRows-2
        out = ""
        length = len(s)

        for r in range(numRows):
            for i in range(r,length,jump):
                out += s[i]
                if (r > 0 and r < numRows-1) and ((i+jump-(2*r)) < length):
                    out += s[i+jump-2*r]

        return out