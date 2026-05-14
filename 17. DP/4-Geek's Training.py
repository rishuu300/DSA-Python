class Solution:
    def recursion(self, arr, day, last):
        if day == 0:
            max_points = -1
            for task in range(3):
                if task != last:
                    max_points = max(max_points, arr[0][task])
            return max_points
        
        max_points = -1
        for task in range(3):
            if task != last:
                points = arr[day][task] + self.recursion(arr, day-1, task)
                max_points = max(max_points, points)
        return max_points
    
    
    def memo(self, arr, day, last, dp):
        if dp[day][last] != -1:
            return dp[day][last]
        
        if day == 0:
            max_points = -1
            for task in range(3):
                if task != last:
                    max_points = max(max_points, arr[0][task])
            
            dp[day][last] = max_points
            return dp[day][last]
        
        max_points = -1
        for task in range(3):
            if task != last:
                points = arr[day][task] + self.memo(arr, day-1, task, dp)
                max_points = max(max_points, points)
        
        dp[day][last] = max_points
        return dp[day][last]
    
    
    def table(self, arr, n):
        dp = [[0] * 4 for _ in range(n)]
        
        dp[0][0] = max(arr[0][1], arr[0][2])
        dp[0][1] = max(arr[0][0], arr[0][2])
        dp[0][2] = max(arr[0][0], arr[0][1])
        dp[0][3] = max(arr[0][0], max(arr[0][1], arr[0][2]))
        
        for day in range(1, n):
            for last in range(4):
                
                max_points = -1
                
                for task in range(3):
                    if task != last:
                        points = arr[day][task] + dp[day-1][task]
                        max_points = max(max_points, points)
                
                dp[day][last] = max_points
        
        return dp[n-1][3]
    
    
    def space(self, arr, n):
        dp = [0]*4
        
        dp[0] = max(arr[0][1], arr[0][2])
        dp[1] = max(arr[0][0], arr[0][2])
        dp[2] = max(arr[0][0], arr[0][1])
        dp[3] = max(arr[0][0], max(arr[0][1], arr[0][2]))
        
        for day in range(1, n):
            
            temp_dp = [0]*4
            
            for last in range(4):
                
                max_points = -1
                
                for task in range(3):
                    if task != last:
                        points = arr[day][task] + dp[task]
                        max_points = max(max_points, points)
                
                temp_dp[last] = max_points
            
            dp = temp_dp.copy()
        
        return dp[3]
    
    def maximumPoints(self, arr):
        n = len(arr)
        
        # return self.recursion(arr, len(arr)-1, 3)
        
        # dp = [[-1] * 4 for _ in range(n)]
        # return self.memo(arr, n-1, 3, dp)
        
        # return self.table(arr, n)
        
        return self.space(arr, n)