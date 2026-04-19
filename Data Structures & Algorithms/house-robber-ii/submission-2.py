class Solution:
    def rob(self, nums: List[int]) -> int:

        # mio tentativo

        """
        1) Edge cases like empty inputs
        2) Dynamic programming solution
        """

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):

        rob1, rob2 = 0, 0
        for n in nums:
            newRob = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = newRob

        return rob2
        
        """
        3) Syntax and dry run: seems ok
        4) Time complexity O(n); space complexity O(1)
        """


        