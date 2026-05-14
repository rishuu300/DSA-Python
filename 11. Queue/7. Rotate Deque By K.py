from collections import deque

class Solution:    
    def rotateDeque(self, dq, type, k):
        if type == 1:
            for _ in range(k):
                dq.appendleft(dq.pop())
        else:
            for _ in range(k):
                dq.append(dq.popleft())