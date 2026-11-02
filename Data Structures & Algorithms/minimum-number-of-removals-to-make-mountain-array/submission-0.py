class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:

        if len(nums) <= 2:
            return -1
        
        n = len(nums)
        up = [1] * n
        down = [1] * n

        # up[i] = len({longest increasing subsequence terminating at i})
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]: 
                    up[i] = max(up[i], up[j] + 1)

        # down[i] = len({longest decreasing subsequence starting at i})
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if nums[j] < nums[i]: 
                    down[i] = max(down[i], down[j] + 1)

        return n - max(up[i] + down[i] - 1 for i in range(n) if up[i] > 1 and down[i] > 1)

        """
        - Time complexity O(n**2), where n = len(nums)
        - Space complexity O(n)
        """