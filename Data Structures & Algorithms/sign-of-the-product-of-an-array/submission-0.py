class Solution:
    def arraySign(self, nums: List[int]) -> int:

        if not nums:
            return 0

        prod = 1
        
        for n in nums:
            prod *= n

        res = float('inf')

        if prod > 0:
            res = 1
        elif prod < 0:
            res = -1
        else:
            res = 0

        return res

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(1).
"""