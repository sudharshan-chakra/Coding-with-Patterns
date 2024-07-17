class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split('.')
        version2 = version2.split('.')

        l,r = 0,0

        while l<len(version1) or r<len(version2):

            curv1 = int(version1[l]) if l < len(version1) else 0
            curv2 = int(version2[r]) if l < len(version2) else 0

            if curv1 > curv2: 
                return 1 
            elif curv1 < curv2:
                return -1 

            l,r = l+1,r+1
        
        return 0