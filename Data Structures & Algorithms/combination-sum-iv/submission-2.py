class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0

        dp = [0] * (target + 1)
        dp[0] = 1

        for a in range(target + 1):
            for n in nums:
                if a - n >= 0:
                    dp[a] += dp[a - n]

        return dp[target]  

        """
        Time complexity O(n), where n = len(nums); space complexity O(1)
        """