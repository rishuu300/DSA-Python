class Solution:
    def minAdjDifference(arr, n):
        if (n < 2): return

        res = abs(arr[1] - arr[0])
        
        for i in range(2, n):
            res = min(res, abs(arr[i] - arr[i - 1]))

        res = min(res, abs(arr[n - 1] - arr[0])) 
        
        return res