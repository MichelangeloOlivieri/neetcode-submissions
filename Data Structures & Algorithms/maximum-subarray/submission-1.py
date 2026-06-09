class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        res = -float('inf')
        l = 0
        r = 0
        amount = 0

        while r < len(nums):
            
            amount += nums[r]
            res = max(res, amount)
            if amount <= 0:
                l = r + 1
                r = l
                amount = 0
            else:
                r += 1

        return res