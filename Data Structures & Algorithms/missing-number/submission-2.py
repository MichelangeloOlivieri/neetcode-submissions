class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        """
        1) Empty input
        2) XOR operator
        """

        if not nums:
            return 0

        res = 0
        for n in range(0, len(nums) + 1):
            res = res ^ n
        for n in nums:
            res = res ^ n

        return res

        """
        3) Ok
        4) Time complexity O(n); space complexity O(1)
        """


            
