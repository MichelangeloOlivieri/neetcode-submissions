class Solution:
    def rob(self, nums: List[int]) -> int:

        # mio tentativo

        """
        1) Edge cases like empty inputs
        2) Dynamic programming solution
        """

        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        return max(self.houseRobberI(nums[:-1]), self.houseRobberI(nums[1:]))

    def houseRobberI(self, array):
        if not array:
            return None
        if len(array) == 1:
            return array[0]
        if len(array) == 2:
            return max(array[0], array[1])

        dp = [0] * len(array)
        dp[0] = array[0]
        dp[1] = max(array[0], array[1])
        for i in range(2, len(array)):
            dp[i] = max(array[i] + dp[i - 2], dp[i - 1])

        return dp[len(array) - 1]

        """
        3) Syntax and dry run: seems ok
        4) Time complexity O(n); space complexity O(1)
        """


        