class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        '''
        * The brute force approach is to check all the other intervals other than i
        and that gives a complexity of O(n^2)
        * But if we sort by start time and max end time (x[0], -x[1]) we can always 
        ensure that any other interval won't cover the first interval 
        * This helps us to start the list and compare each upcoming interval with the latest one 
        on the list
        '''
        intervals.sort(key = lambda x: (x[0],-x[1]))
        out = [intervals[0]]

        for start, end in intervals[1:]:
            prev_start, prev_end = out[-1]

            if start >= prev_start and end <= prev_end:
                continue
            out.append([start, end])

        return len(out) 