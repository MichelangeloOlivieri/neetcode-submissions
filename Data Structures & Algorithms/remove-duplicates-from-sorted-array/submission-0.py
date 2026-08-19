class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        """
        1) nums = [1, 1, 1, 2, 3, 3, 4] -> 4
        nums = [1, 2, 3, 4, 3, 3, 4]
        2) Array, Two Pointers
        """
        
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        count = 0
        l = 0
        r = 0
        i = 0

        while l < len(nums):
            r += 1
            while r < len(nums) and nums[r] == nums[l]:
                count += 1
                r += 1
            l = r
            i += 1
            if i < len(nums) and r < len(nums):
                nums[i] = nums[r]        

        return len(nums) - count

        """
        3) nums = [1, 2, 1, 2, 3, 3, 4], count = 0
        -> i = 0:
        - j = 1, count = 1
        - j = 2, count = 2
        - j = 3, i = 3
        -> i = 3: i = 4
        -> i = 4: 
        - j = 5, count = 3
        - j = 6, i = 6
        4) Time complexity O(n), where n = len(nums); space complexity O(1)
        """