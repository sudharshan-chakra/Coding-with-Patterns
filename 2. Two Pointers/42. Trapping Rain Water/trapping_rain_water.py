class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxL = [0] * length
        maxR = [0] * length

        maxl = 0
        for i in range(1,length):
            maxl = max(height[i-1],maxl)
            maxL[i] = maxl
        
        maxr = 0
        for i in range(length-2,-1,-1):
            maxr = max(height[i+1],maxr)
            maxR[i] = maxr
        
        count = 0
        for i in range(length):
            val = min(maxL[i],maxR[i]) - height[i]
            if val > 0:
                count += val
        
        return count