class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # soluzione dfs + memoization

        memo = {}

        def dfs(rem):

            if rem == 0:
                return 0
            elif rem < 0:
                return float('inf')
            elif rem in memo:
                return memo[rem]

            min_coins = float('inf')
        
            for c in coins:
                res = dfs(rem - c)
                if res != float('inf'):
                    min_coins = min(min_coins, 1 + res)
            
            memo[rem] = min_coins
            return min_coins

        risultato = dfs(amount)
        return risultato if risultato != float('inf') else -1 
        