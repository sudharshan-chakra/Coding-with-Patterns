class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        print(intervals)
        out = [intervals[0]]

        for i in range(1,len(intervals)):
            prev_end = out[-1][1]
            start, end = intervals[i]

            if prev_end >= start:
                out[-1][1] = max(prev_end, end)
            else:
                out.append([start, end])
            
        return out