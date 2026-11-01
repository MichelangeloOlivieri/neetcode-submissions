class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        # even = total sum of the best subsequence terminating with an addition
        even = 0
        # odd = total sum of the best subsequence terminating with a subtraction
        odd = 0

        for x in nums:
            even, odd = max(even, odd + x), max(odd, even - x)

        return even

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """
