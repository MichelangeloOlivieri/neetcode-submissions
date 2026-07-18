class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        """
        nums = [10, 5, -1, 20] -> 35
        """
    
        if not nums:
            return 0

        max_sum = -float('inf')
        max_length = len(nums)

        for i in range(len(nums)):
            cur_sum = 0
            cur_length = 1
            while cur_length <= max_length:
                if cur_sum >= 0:
                    cur_sum += nums[i]
                else:
                    cur_sum = nums[i]
                max_sum = max(max_sum, cur_sum)

                i += 1
                if i == len(nums):
                    i = 0
                cur_length += 1

        return max_sum

        """
        Time complexity O(n^2); space complexity O(1)
        """