class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:

        if not grid or grid[0][0] == 1:
            return 0

        m = len(grid)
        n = len(grid[0])
        memo = {}

        def dfs(i, j):
            if i == m or j == n or grid[i][j] == 1:
                return 0
            if i == m - 1 and j == n - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]

        return dfs(0, 0)

        """
        - Time complexity O(m * n)
        - Space complexity O(m * n)
        """