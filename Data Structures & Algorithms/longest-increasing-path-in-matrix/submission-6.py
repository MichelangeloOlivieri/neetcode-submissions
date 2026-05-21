class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        """
        1) Empty input
        2) Dfs with memo
        """
        
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        res = 0
        memo = {}
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            max_path = 1
            for di, dj in directions:
                if (i + di in range(m)
                    and j + dj in range(n)
                    and matrix[i + di][j + dj] > matrix[i][j]):
                        max_path = max(max_path, 1 + dfs(i + di, j + dj)) # guardo il percorso da dove sono verso la fine

            memo[(i, j)] = max_path
            return max_path

        for i in range(m):
            for j in range(n):
                max_length = dfs(i, j)
                res = max(res, max_length)

        return res

        """
        3) Ok
        4) Time complexity O(m * n); space complexity O(m * n)
        """
            
            
