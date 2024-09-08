class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = -1
        length = len(heights)
        out = []

        for i in range(length-1,-1,-1):
            if heights[i] > max_height:
                max_height = heights[i]
                out.append(i)
        
        return reversed(out)