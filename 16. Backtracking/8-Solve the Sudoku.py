class Solution:
    def solveSudoku(self, mat):
        self.solve(mat)
    
    def solve(self, mat):
        for row in range(len(mat)):
            for col in range(len(mat)):
                
                if mat[row][col] == 0:
                    
                    for i in range(1, 10):
                        if self.isValid(mat, row, col, i):
                            mat[row][col] = i
                            
                            if self.solve(mat):
                                return True
                            else:
                                mat[row][col] = 0
                    
                    return False
        
        return True
    
    def isValid(self, mat, row, col, value):
        for i in range(9):
            if mat[row][i] == value:
                return False
            
            if mat[i][col] == value:
                return False
            
            if mat[3 * (row//3) + (i//3)][3 * (col//3) + (i%3)] == value:
                return False
        
        return True