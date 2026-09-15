class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        res = -float('inf')
        amount = 0

        for n in nums:
            amount += n
            res = max(res, amount)
            if amount <= 0:
                amount = 0

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """