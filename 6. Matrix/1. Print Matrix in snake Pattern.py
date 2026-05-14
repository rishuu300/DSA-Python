class Solution:
    def snakePattern(self, matrix):
        n = len(matrix)
        res = []
        
        for i in range(n):
            if i % 2 == 0:
                for j in range(n):
                    res.append(matrix[i][j])
            else:
                for j in range(n-1, -1, -1):
                    res.append(matrix[i][j])
        
        return res