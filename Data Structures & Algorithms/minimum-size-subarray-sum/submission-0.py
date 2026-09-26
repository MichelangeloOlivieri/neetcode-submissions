class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        """
        1) nums = [10, 3, 2, 4, 1], target = 4
                         ^L^R
        nums = [1, 3, 2, 4, 1]
        2) Two Pointers 
        """

        if not nums:
            return 0

        res = float('inf')
        l = 0
        r = 0
        total = 0

        while r < len(nums):
            while r < len(nums) and total < target:
                total += nums[r]
                r += 1
            while l < r and total >= target:
                res = min(res, r - l)
                total -= nums[l]
                l += 1

        return res if res != float('inf') else 0

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """