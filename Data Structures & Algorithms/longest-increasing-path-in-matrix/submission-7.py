class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])
        res = 0
        memo = {}
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if (r, c) in memo:
                return memo[(r, c)]

            max_path = 1
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if (new_r >= 0 and new_r < m
                and new_c >= 0 and new_c < n
                and matrix[new_r][new_c] > matrix[r][c]):
                    max_path = max(max_path, 1 + dfs(new_r, new_c))

            memo[(r, c)] = max_path
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
            
            
