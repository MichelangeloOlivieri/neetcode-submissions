class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        if not piles:
            return 0
            
        memo = {}

        def dfs(alice: bool, i: int, M: int) -> int:
            if (alice, i, M) in memo:
                return memo[(alice, i, M)]
                
            if i == len(piles):
                return 0

            res = 0 if alice else float('inf')
            total = 0

            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                    
                total += piles[i + X - 1]
                
                if alice:
                    res = max(res, total + dfs(not alice, i + X, max(M, X)))
                else:
                    res = min(res, dfs(not alice, i + X, max(M, X)))

            memo[(alice, i, M)] = res
            return res

        return dfs(True, 0, 1)

        """
        Time complexity O(n^3), where n = len(piles); space complexity O(n^2)
        """