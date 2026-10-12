class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        ans = []
        for i in range(2 * len(nums)):
            i %= len(nums)
            ans.append(nums[i])

        return ans

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """       