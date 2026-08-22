class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        n_red = freq[0]
        for i in range(n_red):
            nums[i] = 0

        n_white = freq[1]
        for i in range(n_red, n_red + n_white):
            nums[i] = 1

        n_blue = freq[2]
        for i in range(n_red + n_white, n_red + n_white + n_blue):
            nums[i] = 2 

        """
        nums = [0, 0, 0, 2]
        - freq = {0 : 3, 1 : 0, 2 : 1}; n_red = 3, n_white = 0, n_blue = 1
        - nums = [0, 0, 0, 2]
        Time complexity O(n), where n = len(nums); space complexity O(n)
        """                   