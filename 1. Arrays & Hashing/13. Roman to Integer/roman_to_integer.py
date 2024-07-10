class Solution:
    def romanToInt(self, s: str) -> int:
        hmap = {
            "I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000
        }
        total = 0
        length = len(s)

        for k in range(length):
            if k < length-1 and hmap[s[k]] < hmap[s[k+1]]:
                total -= hmap[s[k]]
            else:
                total += hmap[s[k]]
        return total
    