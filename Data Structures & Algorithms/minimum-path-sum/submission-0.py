class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        if not grid:
            return 0

        m = len(grid)
        n = len(grid[0])
        directions = [(1, 0), (0, 1)]
        memo = {}

        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return float('inf')
            if i == m - 1 and j == n - 1:
                return grid[i][j]
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = grid[i][j] + min(dfs(i + 1, j), dfs(i, j + 1))
            return memo[(i, j)]

        return dfs(0, 0)

        """
        - Time complexity O(m * n)
        - Space complexity O(m * n)
        """
        