class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        1) Edge cases like nums is None
        2) DP solution
        """

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[len(nums) - 1]

        """
        3) Dry run and syntax: - nums = [1, 0 1, 5], len(nums) = 4;
        - dp[0] = 1, dp[1] = 1, dp[2] = 2, dp[3] = 6
        4) Time complexity O(n); space complexity O(n)
        """