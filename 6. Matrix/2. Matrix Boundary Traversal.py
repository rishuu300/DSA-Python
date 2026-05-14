class Solution:
    def boundaryTraversal(self, mat):
        n, m = len(mat), len(mat[0])
        res = []
        
        if n == 1:
            for i in range(m):
                res.append(mat[0][i])
        elif m == 1:
            for i in range(n):
                res.append(mat[i][0])
        else:
            for i in range(m):
                res.append(mat[0][i])
            
            for i in range(1, n):
                res.append(mat[i][m-1])
            
            for i in range(m-2, -1, -1):
                res.append(mat[n-1][i])
            
            for i in range(n-2, 0, -1):
                res.append(mat[i][0])
        
        return res