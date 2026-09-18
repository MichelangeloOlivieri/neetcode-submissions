class Solution:
    def rob(self, nums: List[int]) -> int:

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        memo = {}

        def dfs(i, flag):
            if i >= len(nums) or (i == len(nums) - 1 and flag):
                return 0
            if (i, flag) in memo:
                return memo[(i, flag)]

            skip = dfs(i + 1, flag)
            steal = nums[i] + dfs(i + 2, flag)
            memo[(i, flag)] = max(skip, steal)

            return memo[(i, flag)]

        return max(dfs(0, True), dfs(1, False))