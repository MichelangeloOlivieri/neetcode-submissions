class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if not edges:
            return 0
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        res = 0
        visited = set()

        def dfs(u):

            visited.add(u)
            for nei in graph[u]:
                if nei not in visited:
                    dfs(nei)

            return 1

        for u in graph:
            if u not in visited:
                res += dfs(u)

        for i in range(n):
            if i not in graph:
                res += 1

        return res
        