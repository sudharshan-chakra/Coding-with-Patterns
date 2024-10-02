class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lens,lent = len(s),len(t)
        l,r = 0,0

        while l < lens and r < lent:
            if s[l] == t[r]:
                l += 1
            r += 1
            
        if l >= lens:
            return True
        if r >= lent:
            return False