class Solution:
    def jump(self, nums: List[int]) -> int:

        memo = {}
        
        def dfs(i):
            if i == len(nums) - 1:
                return 0
            if i >= len(nums):
                return float('inf')
            if i in memo:
                return memo[i]

            min_jumps = float('inf')
            for j in range(1, nums[i] + 1):
                min_jumps = min(min_jumps, 1 + dfs(i + j))

            memo[i] = min_jumps
            return memo[i]

        return dfs(0)

"""
- Time complexity: O(n * max(nums)).
- Space complexity O(n)
"""