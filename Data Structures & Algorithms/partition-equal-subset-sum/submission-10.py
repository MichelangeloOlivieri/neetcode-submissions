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

            if partial_sum > total//2:
                return False
            if partial_sum == total//2:
                return True

            if (start, partial_sum) in memo:
                return memo[(start, partial_sum)]
            
            for end in range(start + 1, len(nums)):
                if dfs(end, partial_sum + nums[end]):
                    return True

            memo[(start, partial_sum)] = False
            return False

        for i in range(len(nums)):
            if dfs(i, nums[i]):
                return True
        
        return False

        """
        3) Syntax and dry run: ok
        4) Time complexity O(n^2 * total); space complexity O(n * total)
        """

