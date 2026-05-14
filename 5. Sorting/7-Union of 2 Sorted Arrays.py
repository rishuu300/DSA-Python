class Solution:
    def findUnion(self, a, b):
        s = set()
        
        for element in a:
            s.add(element)
        
        for element in b:
            s.add(element)
        
        res = list(s)
        
        res.sort()
        
        return res