class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        """
        1) nums = [3, 6, 3], target = 6 -> 5
        2) Array, Backtracking
        """

        if not nums:
            return 0

        memo = {}

        def dfs(amount):
            if amount == target:
                return 1
            if amount > target:
                return 0
            if amount in memo:
                return memo[amount]

            res = 0
            for i in range(len(nums)):
                res += dfs(amount + nums[i])
            
            memo[amount] = res
            return memo[amount]

        return dfs(0)

        """
        3) nums = [3, 6, 3], target = 6
        - res = 0
        - 0 -> 0 -> res += 1
            -> 1 -> NO
            -> 2 -> res += 1
          1 -> res += 1
          2 -> 0 -> res += 1
            -> 1 -> NO
            -> 2 -> res += 1
        4) Time complexity O(n!) where n = len(nums); space complexity O(n)
        """