class Solution:
    def primeDigits(self, n):
        count, number = 0, 1
        
        while count < n:
            if self.onlyPrime(number):
                count += 1
            number += 1
        
        return number-1
    
    def onlyPrime(self, num):
        while num != 0:
            digit = num % 10
            
            if digit != 2 or digit != 3 or digit != 5 or digit != 7:
                return False
            
            num //= 10
        
        return True

# Efficient Solution
from collections import deque

class Solution:
    def primeDigits(self, n):
        q = deque()
        q.append(2)
        q.append(3)
        q.append(5)
        q.append(7)
        
        count, result = 0, 0
        
        while count < n:
            result = q.popleft()
            count += 1
            
            if count == n:
                return result
            
            q.append(result * 10 + 2)
            q.append(result * 10 + 3)
            q.append(result * 10 + 5)
            q.append(result * 10 + 7)
        
        return result