class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = [intervals[0]]
        length = len(intervals)

        for i in range(1,length):
            prev_end = out[-1][1]
            start, end = intervals[i]

            if prev_end >= start:
                out[-1][1] = max(prev_end, end)
            else:
                out.append([start, end])
        
        return out