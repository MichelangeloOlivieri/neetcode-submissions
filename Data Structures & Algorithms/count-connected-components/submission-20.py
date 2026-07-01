class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        res = 0

        graph = {}
        for i in range(n):
            graph[i] = []
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(u):
            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    dfs(nei)

            return 1

        for i in graph:
            if i not in visited:
                res += dfs(i)

        return res

        """
        Time complexity O(V + E); space complexity O(V + E)
        """

        