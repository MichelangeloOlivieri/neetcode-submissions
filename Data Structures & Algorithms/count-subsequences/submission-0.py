class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        if len(s) < len(t):
            return 0

        memo = {}

        def dfs(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] == t[j]:
                memo[(i, j)] = dfs(i + 1, j + 1) + dfs(i + 1, j)
            else: 
                memo[(i, j)] = dfs(i + 1, j)

            return memo[(i, j)]

        return dfs(0, 0)

        """
        Time complexity O(m * n), where m = len(s), n = len(t); space complexity 
        O(m * n)
        """