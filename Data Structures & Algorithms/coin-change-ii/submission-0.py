class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        """
        1) Empty input; example written
        2) Dfs with memoization
        """

        if not coins:
            return 0

        memo = {}

        def dfs(i, total):
            if i == len(coins) or total > amount:
                return 0
            if total == amount:
                return 1
            if (i, total) in memo:
                return memo[(i, total)]

            include = dfs(i, total + coins[i])
            exclude = dfs(i + 1, total)
            memo[(i, total)] = include + exclude

            return memo[(i, total)]

        return dfs(0, 0)

        """
        3) Ok
        4) Time complexity O(n * m), where n = len(coins) and m = amount; space 
        complexity O(n * m)
        """

        