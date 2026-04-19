class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # tentativo mio

        """
        1) It's a classical problem, so not much to worry about apart from edge cases such as
        nums = [] or target not in nums
        2) Binary search algorithm
        """

        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1

        return -1

        """
        3) Dry run: - nums = [-3, 2, 4, 5, 10]; target = 10; 
        - l = 0; r = 4; mid = 2; nums[2] = 4 < 10 = target; l = 3
        - l = 3; r = 4; mid = 3; nums[3] = 5 < 10 = target; l = 4
        - l = 4; r = 4; mid = 4; nums[4] = 10 = 10 = target
        - nums = [-3, 2, 4, 5, 10]; target = -3
        - l = 0; r = 4; mid = 2; nums[2] = 4 > -3 = target; r = 1
        - l = 0; r = 1; mid = 1; nums[1] = 2 > -3 = target; r = 0
        - l = 0; r = 0; mid = 0; nums[0] = -3 = -3 = target
        4) Time complexity O(log(n)) (because at each time we half the interval, so we have at
        most 1/2^k = 1 passages and thus k = log_2(n)); space complexity O(1)
        """