class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        """
        1) nums = [3, 3, 2, 1, 2, 1, 1] -> 2
        --- max&max = max > n >= max&n ---
        2) Find the longest chain of maximum values and return its length
        """

        if not nums:
            return 0
        
        maximum = max(nums)
        res = 0
        length = 0

        for n in nums:
            length = length + 1 if n == maximum else 0
            res = max(res, length)

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """
