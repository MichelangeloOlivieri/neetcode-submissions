class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        """
        1) Empty input, 32-bit integer output
        2) Dfs solution would work; I think it is even efficient as you have to check every 
        single possibility; also a bottom-up solution with dp would work
        """

        # edge cases

        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1

        # dfs implementation
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == m - 1 or j == n - 1:
                return 1

            memo[(i, j)] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[(i, j)]

        return dfs(0, 0)

        """
        3) Syntax and dry run: ok
        4) Time complexity O(m * n); space complexity O(m x n)
        """
        

        


        