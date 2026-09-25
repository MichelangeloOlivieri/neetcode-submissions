class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        ans = []
        for n in nums:
            ans.append(n)
        for n in nums:
            ans.append(n)

        return ans

        """
        - Time complexity O(n), where n = len(nums)
        - Space complexity O(1)
        """       