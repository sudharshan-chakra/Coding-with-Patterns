class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check = [0] * 26

        for ch in s:
            check[ord(ch)-97] += 1
        
        for ch in t:
            check[ord(ch)-97] -= 1
        
        for n in check:
            if n != 0:
                return False
        
        return True