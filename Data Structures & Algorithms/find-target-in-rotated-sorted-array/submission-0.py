class Solution:
    def search(self, nums: List[int], target: int) -> int:

        """
        1) The problem is the same as the one before, so same questions as before
        2) - Solution 1: binary search algorithm
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            if nums[mid] >= nums[l]:
                if target >= nums[l]:
                    if target > nums[mid]:
                        l = mid + 1
                    else: 
                        r = mid - 1
                else: 
                    l = mid + 1

            else: 
                if target <= nums[r]:
                    if target > nums[mid]:
                        l = mid + 1
                    else: 
                        r = mid - 1
                else: 
                    r = mid - 1

        return -1


        """
        3) Dry run: ok
        4) Time complexity O(n); space complexity O(1)
        """
        