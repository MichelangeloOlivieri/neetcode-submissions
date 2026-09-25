class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        if not nums:
            return 0

        if target > nums[-1]:
            return len(nums)
        if target < nums[0]:
            return 0

        l = 0
        r = len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                return mid

        return l

        """
        - Time complexity O(log(n)), where n = len(nums)
        - Space complexity O(1)
        """