class Solution:
    def balanceSums(self, mat):
        n = len(mat)
        maxSum = 0
        rowSum, colSum = [0]*n, [0]*n
        
        for i in range(n):
            for j in range(n):
                rowSum[i] += mat[i][j]
                colSum[j] += mat[i][j]
                
                maxSum = max(maxSum, rowSum[i])
                maxSum = max(maxSum, colSum[j])
        
        rowMax, colMax = 0, 0
        
        for i in range(n):
            rowMax += maxSum - rowSum[i]
            colMax += maxSum - colSum[i]
        
        return max(rowMax, colMax)