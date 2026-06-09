class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # è equivalente alla precedente

        if not nums:
            return 0

        res = -float('inf')
        amount = 0

        i = 0
        while i < len(nums):
            
            amount += nums[i]
            res = max(res, amount)
            
            if amount <= 0:
                amount = 0

            i += 1

        return res