from collections import deque

class Solution:
    def reverseFirstK(self, q, k):
        n = len(q)
        dq = deque()
        
        if k > n:
            return q
        
        for _ in range(k):
            dq.append(q.popleft())
        
        for _ in range(k):
            q.append(dq.pop())
        
        for _ in range(n - k):
            q.append(q.popleft())
        
        return q