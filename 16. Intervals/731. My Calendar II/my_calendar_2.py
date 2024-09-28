class MyCalendarTwo:

    def __init__(self):
        self.overlap = []
        self.non_overlap = []

    def is_overlap(self,pstart,pend,start,end):
        return not (end <= pstart or start >= pend) 

    def book(self, start: int, end: int) -> bool:
        
        # check in the overlap array - for triple booking
        for ostart, oend in self.overlap:
            if self.is_overlap(ostart,oend,start,end):
                return False
        
        # add the overlap regions to the overlap array
        for pstart, pend in self.non_overlap:
            if self.is_overlap(pstart, pend, start, end):
                self.overlap.append([max(pstart,start),min(pend,end)])

        self.non_overlap.append([start, end])
        return True



# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)