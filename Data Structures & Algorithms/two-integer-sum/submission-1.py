class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # soluzione ottimizzata con hash map

        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i

        """
        Test case: - nums = [3, 4, 5, 6], target = 7
        - i = 0, n = 3; diff = 4; prevMap[3] = 0;
        - i = 1, n = 4; diff = 3 che è in prevMap
        """