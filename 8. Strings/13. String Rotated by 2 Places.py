class Solution:
    def isRotated(self,s1,s2):
        n = len(s1)
        a = True
        b = True
        
        for i in range(n):
            if s1[i] != s2[(i+2)%n]:
                a = False
                break
        
        for i in range(n):
            if s1[i] != s2[(i-2)%n]:
                b = False
                break
        
        return a or b