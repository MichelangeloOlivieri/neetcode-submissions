class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        """
        1) nums = [2, 2], k = 5 -> True
            nums = [7, 1, 7], k = 1 -> False
        2) Array, Brute Force (Hash Map)
        """

        if not nums:
            return False

        index = {}

        for i, n in enumerate(nums):
            if n in index and abs(index[n] - i) <= k:
                return True
            else:
                index[n] = i

        return False

        """
        3) a. nums = [2, 2], k = 5, index = {}: 
        - i = 0, n = 2: index = {2 : 0}
        - i = 1, n = 2: True
        b. nums = [7, 1, 7], k = 2, index = {}:
        - i = 0, n = 7: index = {7 : 0}
        - i = 1, n = 1: index = {7 : 0, 1 : 1}
        - i = 2, n = 7: index = {7 : 2, 1 : 1}
        4) Time complexity O(n), where n = len(nums); space complexity O(n)
        """
