class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        res = -float('inf')
        amount = 0

        for i in range(len(nums)):
            amount += nums[i]
            if amount >= 0:
                res = max(res, amount)
            else:
                res = max(res, amount)
                amount = 0

        return res
            

        