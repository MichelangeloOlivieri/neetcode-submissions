class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        """
        1) nums = [1, 2, 3, 4], k = 2 -> nums = [3, 4, 1, 2]
        2) Index Manipulation
        """

        if not nums:
            return None

        copy = [0] * len(nums)

        for i in range(len(nums)):
            copy[(k + i) % len(nums)] = nums[i] 

        for i in range(len(nums)):
            nums[i] = copy[i]     

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """  