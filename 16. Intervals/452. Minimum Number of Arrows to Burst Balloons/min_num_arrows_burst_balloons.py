class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev_end = points[0][1]
        length = len(points)
        count = 1

        for start, end in points[1:]:
            
            if start <= prev_end:
                prev_end = min(end, prev_end)
            else:
                prev_end = end
                count += 1
        
        return count