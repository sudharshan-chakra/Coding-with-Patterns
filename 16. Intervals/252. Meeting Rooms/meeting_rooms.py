class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x: x[0])
        length = len(intervals)

        for i in range(1, length):
            prev_end = intervals[i-1][1]
            start = intervals[i][0]

            if start < prev_end:
                return False

        return True