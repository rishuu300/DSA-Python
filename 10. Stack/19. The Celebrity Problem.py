class Solution:
    def celebrity(self, mat):
        n = len(mat)
        stack = []
        
        for i in range(n):
            stack.append(i)
        
        while len(stack) > 1:
            a = stack.pop()
            b = stack.pop()
            
            if mat[a][b] == 1:
                stack.append(b)
            else:
                stack.append(a)
        
        celeb = stack[-1]
        zeros, ones = 0, 0
        
        for i in range(n):
            if mat[celeb][i] == 0:
                zeros += 1
            
            if mat[i][celeb] == 1:
                ones += 1
        
        return celeb if zeros == n-1 and ones == n else -1