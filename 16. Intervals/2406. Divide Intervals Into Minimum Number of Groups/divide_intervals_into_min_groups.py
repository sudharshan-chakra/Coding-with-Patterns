class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        groups = 0
        starts, ends = [],[]

        for start,end in intervals:
            starts.append(start)
            ends.append(end)
        
        starts.sort()
        ends.sort()

        s,e = 0,0
        cur = 0

        while s < len(starts) and e < len(ends):
            if starts[s] <= ends[e]:
                cur += 1
                s += 1
            else:
                cur -= 1
                e += 1    
            groups = max(groups,cur) 

        return groups