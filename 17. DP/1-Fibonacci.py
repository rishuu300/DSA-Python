class Solution:
    def nthFibonacci(self, n: int) -> int:
        # return self.recursion(n)
        
        # dp = [-1]*(n+1)
        # return self.memo(n, dp)
        
        # return self.table(n)
        
        return self.space(n)
    
    def recursion(self, n):
        if n == 0 or n == 1:
            return n
        return self.recursion(n-1) + self.recursion(n-2)
    
    def memo(self, n, dp):
        if dp[n] != -1:
            return dp[n]
        
        if n == 0 or n == 1:
            return n
        
        dp[n] = self.memo(n-1, dp) + self.memo(n-2, dp)
        return dp[n]
    
    def table(self, n):
        if n == 0 or n == 1:
            return n
        
        dp = [0]*(n+1)
        dp[0] = 0
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    def space(self, n):
        if n == 0 or n == 1:
            return n
        
        prev1 = 0
        prev = 1
        
        for i in range(2, n+1):
            curr = prev + prev1
            
            prev1 = prev
            prev = curr
        
        return prev