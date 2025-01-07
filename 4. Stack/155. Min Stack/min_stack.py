class MinStack:

    def __init__(self):
        self.min_val = float('inf')
        self.stack = []

    def push(self, val: int) -> None:
        self.min_val = min(self.min_val, val)
        self.stack.append((val,self.min_val))

    def pop(self) -> None:
        self.stack.pop()
        self.min_val = self.stack[-1][1] if self.stack else float('inf')

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]