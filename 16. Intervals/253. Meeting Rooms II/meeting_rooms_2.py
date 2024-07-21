class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts, ends = [], []
        count = l = r = 0
        max_rooms = 0

        for start, end in intervals:
            starts.append(start)
            ends.append(end)

        starts.sort()
        ends.sort()

        while l < len(starts) and r < len(ends):
            if starts[l] < ends[r]:
                count += 1
                l += 1
            else:
                count -= 1
                r += 1

            max_rooms = max(max_rooms, count)

        return max_rooms