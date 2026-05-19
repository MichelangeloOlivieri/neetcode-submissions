class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        """
        1) Empty input; example seen; I understand you have a binary choice for each
        integer: ie you cannot sum or subtract an integer multiple times
        2) Dfs with memoization
        """

        if not nums:
            return 0

        memo = {}

        def dfs(i, total):
            if i == len(nums):
                if total == target:
                    return 1
                else:
                    return 0
            if (i, total) in memo:
                return memo[(i, total)]

            sum_current = dfs(i + 1, total + nums[i])
            subtract_current = dfs(i + 1, total - nums[i])
            memo[(i, total)] = sum_current + subtract_current

            return memo[(i, total)]

        return dfs(0, 0)

        """
        3) Ok
        4) Time complexity O(n * m), where n = len(nums) and m is the sum of all the
        elements in the array; space complexity O(n * m)
        """