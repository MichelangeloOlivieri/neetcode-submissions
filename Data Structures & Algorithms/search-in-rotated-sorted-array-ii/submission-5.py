class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        if not nums:
            return False

        def binary_search(left, right):
            if target < nums[left] or nums[right] < target:
                return False

            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid + 1
                elif target < nums[mid]:
                    right = mid - 1
            
            return False

        l = 0
        r = len(nums) - 1

        while l <= r:
            if nums[l] == target or nums[r] == target:
                return True
            if target < nums[l] and nums[r] < target:
                return False
            if nums[l] < nums[r]:
                return binary_search(l, r)

            l += 1
            r -= 1

        return False

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """