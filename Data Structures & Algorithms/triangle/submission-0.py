class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle or not triangle[0]:
            return 0

        h = len(triangle)
        memo = {}

        def dfs(i, j):
            if i == h:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            left = dfs(i + 1, j)
            right = dfs(i + 1, j + 1)
            memo[(i, j)] = triangle[i][j] + min(left, right)

            return memo[(i, j)]

        return dfs(0, 0)

        """
        - Time complexity O(h**2), where h = len(triangle)
        - Space complexity O(h**2)
        """