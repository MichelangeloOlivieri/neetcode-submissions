class Solution:
    def findMin(self, nums: List[int]) -> int:

        # mio tentativo
        
        """
        1) Usual questions about edge cases like empty inputs and stuff
        2) - Solution 1: scan the array, find out wheter there is a gap or not; in the first
        case return the first element after the gap, else return the first element of the array
        - Solution 2: some kind of variation of binary search algorithm
        """

        l = 0
        r = len(nums) - 1
        res = float('inf')

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            mid = (l + r) // 2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid + 1
            else: 
                r = mid - 1

        return res

        """
        3) Dry run: ok
        4) Time complexity O(log(n)); space complexity O(1)
        """

