class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if not nums: 
            return False
        
        for i in range(len(nums)):
            nums[i] = [nums[i], i]

        nums.sort()

        i = 0
        while i < len(nums):
            j = i + 1
            index = nums[i][1]
            while j < len(nums) and nums[i][0] == nums[j][0]:
                if abs(nums[j][1] - index) <= k:
                    return True
                else: 
                    index = nums[j][1]
                j += 1
            i = j

        return False

        """
        3) a. nums = [2, 1, 2], k = 1:
        - nums = [[2, 0], [1, 1], [2, 2]] -> nums = [[1, 1], [2, 0], [2, 2]]
        - i = 0, j = 1: continue
        - i = 1, j = 2: return True
        """