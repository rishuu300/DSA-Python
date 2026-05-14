from typing import List

class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]):
        S.sort()
        F.sort()
        
        res = 1, count = 1
        i, j = 1, 0
        
        while i < N and j < N:
            if S[i] <= F[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            
            res = max(res, count)
        
        return count