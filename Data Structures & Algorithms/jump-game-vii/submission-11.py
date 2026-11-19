class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:

        # DP: Two Pointers

        n = len(s)
        if s[n - 1] == "1":
            return False
        
        dp = [False] * n
        dp[0] = True
        furthest = 0

        for i in range(n):
            if not dp[i]:
                continue

            start = max(furthest, i + minJump)
            end = min(n, i + maxJump + 1)
            
            for j in range(start, end):
                if s[j] == "0":
                    dp[j] = True
                
            furthest = end - 1

        return dp[n - 1]

    """
    - Time complexity: O(n), where n = len(s).
    - Space complexity: O(n).
    """