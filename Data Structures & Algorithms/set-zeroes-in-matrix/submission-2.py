class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        m = len(matrix)
        n = len(matrix[0])

        def helper(r, c):
            for i in range(m):
                if matrix[i][c] != float('inf'):
                    matrix[i][c] = 0
            for j in range(n):
                if matrix[r][j] != float('inf'):
                    matrix[r][j] = 0
            matrix[r][c] = 0
            
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')
                
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    helper(i, j)


        

        
        
        