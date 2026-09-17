class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:

        """
        1) stoneValue = [10, 1, 1, 1] -> "Alice"
        stoneValue = [1, 1, 1, 10] -> "Bob"
        stoneValue = [1, 1, 1, 1, 1, 1] -> "Tie"
        2) Dynamic Programming
        """
        
        if not stoneValue:
            return "Tie"

        res = -float('inf')
        memo = {}

        def dfs(i):
            if i == len(stoneValue):
                return 0
            if i in memo:
                return memo[i]
            
            amount = -float('inf')
            value = 0
            for j in range(i, min(i + 3, len(stoneValue))):
                value += stoneValue[j]
                amount = max(amount, value - dfs(j + 1))

            memo[i] = amount
            return amount

        res = dfs(0)
        if res > 0:
            return "Alice"
        elif res < 0:
            return "Bob"
        else:
            return "Tie"
        
        """
        - Time complexity O(n)
        - Space complexity O(n)
        """