class MyCalendar:

    def __init__(self):
        self.heap = []

    def book(self, start: int, end: int) -> bool:
        if self.heap == []:
            self.heap.append([start,end])
            return True
        
        for pstart, pend in self.heap:
            if not (start >= pend or end <= pstart):
                return False
        
        self.heap.append([start,end])
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)