class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        if not nums:
            return 0

        current_max = 0
        current_min = 0
        global_max = nums[0]
        global_min = nums[0]
        total_sum = 0

        for n in nums:
            current_max = max(n, current_max + n)
            global_max = max(current_max, global_max)

            current_min = min(n, current_min + n)
            global_min = min(current_min, global_min)

            total_sum += n
        
        if global_max < 0:
            return global_max

        return max(global_max, total_sum - global_min)

        """
        Time complexity O(n); space complexity O(1)
        """