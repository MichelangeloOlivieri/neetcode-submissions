class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        """
        1) stones = [7, 1, 10] -> 7
        stones = [3, 1]
        first = 10
        second = 7
        2) Array, Heap
        """

        if not stones:
            return 0

        total = sum(stones)
        target = (total + 1) // 2
        memo = {}

        def dfs(i, amount):
            if i == len(stones) or amount >= target:
                return abs(amount - (total - amount))
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            choose = dfs(i + 1, amount + stones[i])
            skip = dfs(i + 1, amount)

            memo[(i, amount)] = min(choose, skip)
            return memo[(i, amount)]

        return dfs(0, 0)

        """
        - Time complexity O(n * total), where n = len(stones) and total = sum(stones)
        - Space complexity O(n * total)
        """