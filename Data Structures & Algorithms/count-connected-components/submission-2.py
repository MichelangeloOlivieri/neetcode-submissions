class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        """
        1) Empty input
        2) Dfs approach
        """

        # edge cases

        if not n:
            return 0
        if not edges:
            return n

        # dfs implementation

        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        res = 0

        def dfs(current):
            visited.add(current)
            for nei in graph[current]:
                if nei in visited:
                    continue
                else:
                    dfs(nei)
    
        for i in range(n):
            if i not in visited:
                dfs(i)
                res += 1

        return res

        """
        3) Syntax and dry run: ok
        4) Time complexity O(E + V); space complexity O(V)
        """
        