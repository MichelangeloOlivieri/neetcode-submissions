class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1

        n = len(nums)
        i = 0
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp
                
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

        """
        Time complexity O(n); space complexity O(1)
        """            