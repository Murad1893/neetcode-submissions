from collections import deque

class MinStack:

    def __init__(self):
        # we can maintain a single minimum, but that won't work if popped. Since min changes
        # hence we maintain a second stack to store running min and pop from both
        self.stack = []
        self.min_stack = [] # this maintain running min
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min(val, self.min_stack[-1]))
    
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
