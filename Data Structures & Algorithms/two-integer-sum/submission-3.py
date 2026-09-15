class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in seen:
                return [seen[diff], i]
            seen[n] = i

        return []

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(n)
        """