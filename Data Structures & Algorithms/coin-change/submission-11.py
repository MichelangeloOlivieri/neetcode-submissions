class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        """
        1) coins = [1, 5, 10], amount = 12 -> 3
        2) Array, DP
        """

        if not coins or amount == 0:
            return 0

        memo = {}

        def dfs(a: int) -> int:
            if a == amount: 
                return 0
            if a > amount:
                return float('inf')
            if a in memo:
                return memo[a]

            min_count = float('inf')
            for c in coins:
                count = dfs(a + c)
                if count != float('inf'):
                    min_count = min(1 + count, min_count)

            memo[a] = min_count
            return min_count

        res = dfs(0)
        return res if res != float('inf') else -1