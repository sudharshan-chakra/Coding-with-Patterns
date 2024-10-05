class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        maxL, maxR = 0,0
        count = 0
        l,r = 0,length-1

        while l <= r:
            if maxL <= maxR:
                val = maxL - height[l]
                count += val if val > 0 else 0
                maxL = max(maxL,height[l])
                l += 1
            else:
                val = maxR - height[r]
                count += val if val > 0 else 0
                maxR = max(maxR,height[r])
                r -= 1
        return count