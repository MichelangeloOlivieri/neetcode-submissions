class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        """
        1) Empty input; can one jump less than nums[i] in order to reach the last 
        position?
        2) - Solution 1: dynamic programming starting from the last position
        """

        if not nums:
            return False
        if len(nums) == 1:
            return True

        dp = [False] * len(nums)
        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, min(i + 1 + nums[i], len(nums))):
                if dp[j] == True:
                    dp[i] = True

        return dp[0]   

        """
        3) Syntax and dry run: ok
        4) Time complexity O(n^2); space complexity O(n)
        """    