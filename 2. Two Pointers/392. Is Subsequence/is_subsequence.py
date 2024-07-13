class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l,r = 0,0
        slen, tlen = len(s), len(t)
        
        if not s: return True
        if not t: return False

        while r < tlen and l < slen:
            if s[l] == t[r]:
                l += 1
            r += 1

        return True if l == slen else False
