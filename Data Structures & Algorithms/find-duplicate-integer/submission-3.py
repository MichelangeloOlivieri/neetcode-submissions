class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        new_slow = 0
        while True:
            slow = nums[slow]
            new_slow = nums[new_slow]
            if slow == new_slow:
                return slow

        return -1

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """        
        