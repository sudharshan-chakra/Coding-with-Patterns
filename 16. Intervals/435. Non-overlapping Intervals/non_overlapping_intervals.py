class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        length = len(intervals)
        out = [intervals[0]]

        for i in range(1, length):
            prev_start, prev_end = out[-1]
            start, end = intervals[i]

            if start < prev_end:
                out[-1][1] = min(prev_end, end)
            else:
                out.append([start, end])
        
        return length - len(out)