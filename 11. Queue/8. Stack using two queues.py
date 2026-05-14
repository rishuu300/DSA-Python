from collections import deque

class myStack:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()


    def push(self, a):
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1.append(a)

        while self.q2:
            self.q1.append(self.q2.popleft())


    def pop(self):
        if not self.q1:
            return -1
        return self.q1.popleft()


    def top(self):
        if not self.q1:
            return -1
        return self.q1[0]


    def size(self):
        return len(self.q1)