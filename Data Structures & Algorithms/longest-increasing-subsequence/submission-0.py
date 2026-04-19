class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        """
        1) Empty inputs, input: [1, 2, 0, 3, 1, 2, 4] => output = 4 
        2) Solution 1: dfs solution with memoization
        """

        if not nums:
            return 0

        memo = {}
        def dfs(start):
            if start in memo:
                return memo[start]

            max_length = 1
            for end in range(start + 1, len(nums)):
                if nums[end] > nums[start]:
                    max_length = max(1 + dfs(end), max_length)

            memo[start] = max_length
            return max_length

        res = 1
        for i in range(len(nums)):
            res = max(res, dfs(i))

        return res 