class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        if not nums:
            return False

        total = sum(nums)

        if total % k:
            return False
        
        target = total // k
        used = [False] * len(nums)

        def backtrack(i, k, amount):
            if k == 0:
                return True
            if amount == target:
                return backtrack(0, k - 1, 0)

            for j in range(i, len(nums)):
                if used[j] or amount + nums[j] > target:
                    continue
                else:
                    used[j] = True
                    if backtrack(j + 1, k, amount + nums[j]):
                        return True
                    used[j] = False

            return False

        return backtrack(0, k, 0)

        """
        Time complexity O(k * 2^n), where n = len(nums); space complexity O(n)
        """