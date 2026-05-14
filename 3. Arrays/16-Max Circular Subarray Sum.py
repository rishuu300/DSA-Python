class Solution:
    def kadaneMax(self, arr, n):
        maxEnd = arr[0]
        maxSum = arr[0]
        
        for i in range(1, n):
            maxEnd = max(maxEnd + arr[i], arr[i])
            maxSum = max(maxSum, maxEnd)
        
        return maxSum
    
    def kadaneMin(self, arr, n):
        minEnd = arr[0]
        minSum = arr[0]
        
        for i in range(1, n):
            minEnd = min(minEnd + arr[i], arr[i])
            minSum = min(minSum, minEnd)
        
        return minSum
    
    def maxCircularSum(self, arr):
        n = len(arr)
        maxSum = self.kadaneMax(arr, n)
        
        if maxSum < 0:
            return maxSum
        
        minSum = self.kadaneMin(arr, n)
        
        totalSum = 0
        for i in range(n):
            totalSum += arr[i]
        
        circularMax = totalSum - minSum
        
        return max(maxSum, circularMax)