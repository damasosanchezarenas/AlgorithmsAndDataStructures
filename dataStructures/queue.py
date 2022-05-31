from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def push(self,val):
        self.buffer.appendleft(val)

    def pop(self):
        return self.buffer.pop()

    def peek(self):
        return self.buffer[-1]

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)
