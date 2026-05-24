class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        nums = [1] + nums + [1]
        memo = {}

        def dfs(l, r):
            if l + 1 == r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            max_coins = 0

            for i in range(l + 1, r):
                coins = nums[l] * nums[i] * nums[r]
                total_coins = coins + dfs(l, i) + dfs(i, r)
                max_coins = max(max_coins, total_coins)

            memo[(l, r)] = max_coins
            return memo[(l, r)]

        return dfs(0, len(nums) - 1)

        """
        Time complexity O(n^3), where n = len(nums); space complexity O(n^2)
        """