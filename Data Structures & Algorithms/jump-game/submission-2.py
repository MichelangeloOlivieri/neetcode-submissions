class Solution:
    def canJump(self, nums: List[int]) -> bool:

        if not nums:
            return False

        def dfs(i):
            if i >= len(nums) - 1:
                return True
            elif nums[i] == 0:
                return False

            for j in range(i + 1, i + 1 + nums[i]):
                if dfs(j):
                    return True

            return False 

        return dfs(0)
        