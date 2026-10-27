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
        n = len(nums)
        i = 0
        res = 0

        while i < n:
            length = 0
            while i < n and nums[i] == maximum:
                length += 1
                i += 1

            res = max(res, length)
            i += 1

        return res

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """
