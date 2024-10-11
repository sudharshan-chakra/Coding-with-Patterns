class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len,s2len = len(s1),len(s2)
        s1count, s2count = [0] * 26, [0] * 26
        
        if s1 > s2: return False

        for i in range(s1len):
            s1count[ord(s1[i])-97] += 1
            s2count[ord(s2[i])-97] += 1
        
        if s1count == s2count: return True

        for i in range(s1len,s2len):
            s2count[ord(s2[i])-97] += 1
            s2count[ord(s2[i-s1len])-97] -= 1

            if s1count == s2count: return True
        
        return False
        

