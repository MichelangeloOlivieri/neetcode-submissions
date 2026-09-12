class Solution:
    def integerBreak(self, n: int) -> int:

        """
        1) n = 5 -> 6 (5 = 3 + 2 and 6 = 3 * 2)
        2) Dynamic Programming
        """

        if n == 0 or n == 1:
            return 0

        memo = {}

        def dfs(i):
            if i == 1 or i == 2:
                return 1
            if i in memo:
                return memo[i]

            res = -float('inf')
            for j in range(1, i):
                diff = i - j
                res = max(j * max(dfs(diff), diff), res)

            memo[i] = res
            return memo[i]

        return dfs(n)

        """
        - Time complexity O(n^2)
        - Space complexity O(n)
        """
        