class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # dfs solution with memoization

        """
        1) Empty inputs; do the subsets have to be connected?
        2) Solution 1: dfs with recursion might work but it is inefficient
        """

        # edge cases
        if not nums or len(nums) == 1:
            return False

        total = 0
        for n in nums:
            total += n
        if total % 2 != 0:
            return False

        # implementation
        memo = {}

        def dfs(start, partial_sum):

            if partial_sum > total/2:
                return False
            if partial_sum == total/2:
                return True
            
            partial_sum += nums[start]
            for end in range(start + 1, len(nums)):
                if dfs(end, partial_sum):
                    return True

            return False

        for i in range(len(nums)):
            if dfs(i, 0):
                return True
        
        return False

        """
        3) Syntax and dry run: ok
        4) Time complexity O(2^n); space complexity O(n)
        """

