class Solution:
    def candy(self, ratings: List[int]) -> int:

        memo = {}

        def dfs(i):
            if i in memo:
                return memo[i]

            candies = 1

            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                candies = max(candies, dfs(i - 1) + 1)
            if i + 1 <= len(ratings) - 1 and ratings[i] > ratings[i + 1]:
                candies = max(candies, dfs(i + 1) + 1)

            memo[i] = candies
            return candies

        return sum([dfs(i) for i in range(len(ratings))])

        """
        Time complexity O(n), where n = len(ratings); space complexity O(n)
        """