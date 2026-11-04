class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:

        if not nums1 or not nums2:
            return 0

        dp = [0] * (len(nums2) + 1)

        for x in nums1:
            diagonal = 0
            for j, y in enumerate(nums2, 1):
                old = dp[j]
                dp[j] = diagonal + 1 if x == y else max(dp[j], dp[j - 1])
                diagonal = old

        return dp[-1]

        """
        - Time complexity O(m * n), where m = len(nums1) and n = len(nums2)
        - Space complexity O(n) 
        """
