class Solution:
    def check(self, num):
        while num > 0:
            if num%10 == 1 or num%10 == 2 or num%10 == 3:
                num //= 10
            else:
                return False
        
        return True
    
    def filterByDigits(self, arr):
        res = []
        
        for element in arr:
            if self.check(element):
                res.append(element)
        
        return res