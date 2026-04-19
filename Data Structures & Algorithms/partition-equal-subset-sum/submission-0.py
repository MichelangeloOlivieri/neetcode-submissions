class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # dfs solution

        """
        1) Empty inputs; do the subsets have to be connected?
        2) Solution 1: dfs with recursion might work but it is inefficient
        """

        # edge cases
        if not nums or len(nums) == 1:
            return False

        # implementation
        memo = {}

        def dfs(start, sum1, sum2):
            
            if start == len(nums):
                return sum1 == sum2
            if start in memo:
                return 

            left_result = dfs(start + 1, sum1 + nums[start], sum2)
            right_result = dfs(start + 1, sum1, sum2 + nums[start])

            return left_result or right_result
        
        return dfs(0, 0, 0)

        """
        3) Syntax and dry run: ok
        4) Time complexity O(2^n); space complexity O(n)
        """

