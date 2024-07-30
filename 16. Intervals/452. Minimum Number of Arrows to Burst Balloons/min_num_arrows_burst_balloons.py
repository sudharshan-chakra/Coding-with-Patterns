class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        out = [points[0]]
        length = len(points)

        for start, end in points[1:]:
            prev_start, prev_end = out[-1]

            if start <= prev_end:
                out[-1] = [max(start, prev_start), min(end, prev_end)]
            else:
                out.append([start, end])
        
        return len(out)