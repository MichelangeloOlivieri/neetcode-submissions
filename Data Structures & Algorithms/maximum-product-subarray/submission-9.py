class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        res = max(nums)
        curr_max = 1
        curr_min = 1

        for n in nums:
            if n == 0:
                curr_max = 1
                curr_min = 1
                continue
            else:
                temp = curr_max * n
                curr_max = max(curr_max * n, curr_min * n, n)
                curr_min = min(temp, curr_min * n, n)

            res = max(res, curr_max)

        return res

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(1).
"""