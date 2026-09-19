class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        if not cost:
            return 0    

        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost) + 1):
            current = min(prev2 + cost[i - 2], prev1 + cost[i - 1])
            prev2 = prev1
            prev1 = current

        return current

        """
        - Time complexity O(n), where n = len(cost)
        - Space complexity O(1)
        """