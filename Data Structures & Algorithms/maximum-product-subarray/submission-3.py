class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        """
        1) Empty input
        2) - Solution 1: double index to calculate each single product and return the max
        - Solution 2: dynamic programming solution with mins and maxs
        """

        if not nums:
            return 0
        
        res = max(nums)
        curr_max = curr_min = 1

        for n in nums:
            if n == 0:
                curr_max = curr_min = 1
                continue
            else: 
                temp = curr_max * n
                curr_max = max(curr_max * n, curr_min * n, n)
                curr_min = min(temp, curr_min * n, n)
            res = max(res, curr_max)

        return res

        """
        3) Syntax and dry run: ok
        4) Time complexity O(n); space complexity O(n)
        """
                