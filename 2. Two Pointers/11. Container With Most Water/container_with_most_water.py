class Solution:
    def maxArea(self, height: List[int]) -> int:
        length = len(height)
        l,r = 0,length-1
        max_area = 0

        def area(hl,hr,width):
            return (min(hl,hr)*width)

        while l < r:
            max_area = max(max_area,area(height[l],height[r],r-l))

            if height[l] <= height[r]:
                l += 1
            else:
                r += 1
        
        return max_area
