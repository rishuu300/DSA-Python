class Solution:
    def posOfRightMostDiffBit(self,m,n):
        position = 1
        i = 1
        
        while (m&i) == (n&i):
            position += 1
            i = i<<1
        
        return position