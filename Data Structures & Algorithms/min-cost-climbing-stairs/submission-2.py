class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        """
        1) Empty input; example seen
        2) Dp solution
        """        

        prev2 = 0
        prev1 = 0

        for i in range(2, len(cost) + 1):
            current = min(prev2 + cost[i - 2], prev1 + cost[i - 1])

            prev2 = prev1
            prev1 = current

        return current

        """
        3) Ok
        4) Time complexity O(n); space complexity O(n)
        """