class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(key = lambda x: (x[1]-x[0], x[0]))
        out = []

        for query in queries:
            found = False
            for start, end in intervals:
                if start <= query <= end:
                    out.append(end-start+1)
                    found = True
                    break
            if not found: out.append(-1)
        return out 