class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle or not triangle[0]:
            return 0

        h = len(triangle)
        dp = [0] * (h + 1)

        for i in range(h - 1, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])

        return dp[0]

        """
        - Time complexity O(h**2), where h = len(triangle)
        - Space complexity O(h)
        """