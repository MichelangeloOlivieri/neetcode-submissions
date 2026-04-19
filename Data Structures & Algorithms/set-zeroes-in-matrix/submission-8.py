class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        # invalid solution (but it does work)

        m = len(matrix)
        n = len(matrix[0])

        # right
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(j + 1, n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float('inf')
                    break
        # down
        for j in range(n):
            for i in range(m):
                if matrix[i][j] == 0:
                    for k in range(i + 1, m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = float('inf')
                    break

        # left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == 0:
                    for k in range(j - 1, -1, -1):
                        if matrix[i][k] != 0:
                            matrix[i][k] = float('inf')
                    break

        # up
        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if matrix[i][j] == 0:
                    for k in range(i - 1, -1, -1):
                        if matrix[k][j] != 0:
                            matrix[k][j] = float('inf')
                    break

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0        
        
        """
        Time complexity O(m * n); space complexity O(1)
        """