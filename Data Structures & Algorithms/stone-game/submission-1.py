class Solution:
    def stoneGame(self, piles: List[int]) -> bool:

        memo = {}

        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]

            left = piles[l] - dfs(l + 1, r)
            right = piles[r] - dfs(l, r - 1)

            memo[(l, r)] = max(left, right)
            
            return memo[(l, r)]

        return dfs(0, len(piles) - 1) > 0

        """
        Time complexity O(n^2), where n = len(piles); space complexity O(n^2)
        """