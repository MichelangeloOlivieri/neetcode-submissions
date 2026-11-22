class Solution:
    def checkPossibility(self, nums: list[int]) -> bool:

        if not nums:
            return False

        n = len(nums)

        if n <= 2:
            return True

        changed = False

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                if changed:
                    return False
                if i == 0 or nums[i + 1] >= nums[i - 1]:
                    nums[i] = nums[i + 1]
                else:
                    nums[i + 1] = nums[i]
                changed = True
        return True

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(1).
"""