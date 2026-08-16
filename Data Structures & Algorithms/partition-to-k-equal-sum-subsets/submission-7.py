class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        """
        1) nums = [1, 1, 1], k = 3 -> True
        2) Backtracking, Array problem
        """

        if not nums:
            return False

        total = sum(nums)

        if total % k:
            return False

        target = total // k
        used = [False] * len(nums)

        def backtrack(i, remaining, amount):
            if remaining == 0:
                return True
            if amount == target:
                return backtrack(0, remaining - 1, 0)   

            for j in range(i, len(nums)):
                if used[j] or amount + nums[j] > target:
                    continue
                else:
                    used[j] = True
                    if backtrack(j + 1, remaining, amount + nums[j]):
                        return True
                    used[j] = False

            return False       

        return backtrack(0, k, 0)