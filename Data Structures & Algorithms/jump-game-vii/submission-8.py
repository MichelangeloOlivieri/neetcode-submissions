class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # DP: Sliding Window

        n = len(s)
        dp = [False] * len(s)
        dp[0] = True
        count = 0

        for i in range(1, n):
            # enters window
            if i >= minJump and dp[i - minJump]:
                count += 1
            # exits window
            if i > maxJump and dp[i - maxJump - 1]:
                count -= 1
            if count > 0 and s[i] == "0":
                dp[i] = True

        return dp[n - 1]

    """
    - Time complexity: O(n), where n = len(s).
    - Space complexity: O(n)
    """