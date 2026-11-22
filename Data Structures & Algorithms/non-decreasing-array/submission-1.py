class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        
        if not nums:
            return False

        n = len(nums)

        if n <= 2:
            return True
        
        count = 0 if nums[0] <= nums[1] else 1

        for i in range(2, n - 1):
            if nums[i - 1] > nums[i]:
                if nums[i - 2] <= nums[i]:
                    nums[i - 1] = nums[i]
                elif nums[i - 1] <= nums[i + 1]:
                    nums[i] == nums[i + 1]
                else:
                    return False

                count += 1
                if count == 2:
                    return False

        if nums[n - 2] > nums[n - 1]:
            count += 1
        if count == 2:
            return False

        return True

        """
        [9, 8, 6, 7]
        """

"""
- Time complexity: O(n), where n = len(nums).
- Space complexity: O(1).
"""