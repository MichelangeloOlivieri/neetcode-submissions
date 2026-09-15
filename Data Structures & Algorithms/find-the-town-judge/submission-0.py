class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:

        """
        1) Graph Problem
        2) Topological Sort
        """

        if n == 1:
            return 1

        degree = [0] * (n + 1)
        for u, v in trust:
            degree[u] -= 1
            degree[v] += 1

        for i in range(len(degree)):
            if degree[i] == n - 1:
                return i

        return -1

        """
        - Time complexity O(E + V)
        - Space complexity O(V)
        """