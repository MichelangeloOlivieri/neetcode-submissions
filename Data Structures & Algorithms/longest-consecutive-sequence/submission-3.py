class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numbers_set = set(nums)
        res = 0

        for n in nums:
            if n - 1 not in numbers_set:
                length = 0
                while n + length in numbers_set:
                    length += 1
                res = max(res, length)

        return res        

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """