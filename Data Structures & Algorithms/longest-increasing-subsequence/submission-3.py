class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """
        1) nums = [100, 9, 10, 4, 333, 11, 2, 12] -> 4
        2) DP, Array
        """

        if not nums:
            return 0

        memo = {}
        res = 1

        def dfs(i: int) -> int:
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]

            length = 1
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    length = max(length, 1 + dfs(j))

            memo[i] = length
            return length

        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res

        """
        3) nums = [100, 9, 10, 4, 333, 11, 2, 12]
        - i = 0 -> i = 4
        """