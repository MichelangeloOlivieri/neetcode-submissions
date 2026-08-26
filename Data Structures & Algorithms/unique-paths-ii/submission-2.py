class Solution:
    def uniquePathsWithObstacles(self, grid: list[list[int]]) -> int:

        if not grid or grid[0][0] == 1:
            return 0
            
        m = len(grid)
        n = len(grid[0])
        memo = {}

        def dfs(r, c):
            if r == m or c == n or grid[r][c] == 1:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            if (r, c) in memo:
                return memo[(r, c)]

            memo[(r, c)] = dfs(r + 1, c) + dfs(r, c + 1)
            return memo[(r, c)]

        return dfs(0, 0)

        """
        Time complexity O(m * n); space complexity O(m * n)
        """