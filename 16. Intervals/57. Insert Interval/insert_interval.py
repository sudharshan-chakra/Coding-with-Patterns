class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []

        for i, interval in enumerate(intervals):
            start, end = interval
            new_start, new_end = newInterval

            if new_end < start:
                out.append(newInterval)
                return out + intervals[i:]
            elif end < new_start:
                out.append(interval)
            else:
                newInterval = [min(start, new_start), max(end, new_end)]
        
        out.append(newInterval)        
        return out