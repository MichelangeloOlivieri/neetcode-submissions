class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:
            return 0

        res = -float('inf')
        curr = 0

        for n in nums:
            curr += n
            res = max(res, curr)
            curr = max(0, curr)

        return res

"""
- Time complexity O(n), where n = len(nums)
- Space complexity O(1)
"""