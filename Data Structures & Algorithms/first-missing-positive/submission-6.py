class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        n = len(nums)
        i = 0
        for i in range(n):
            while 1 <= nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                right_index = nums[i] - 1
                nums[i], nums[right_index] = nums[right_index], nums[i]
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """            