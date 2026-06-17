class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not edges:
            return n == 1

        graph = {}
        for i in range(n):
            graph[i] = []
            
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(i, parent):
            if i in visited:
                return True

            visited.add(i)
            for nei in graph[i]:
                if nei != parent and dfs(nei, i):
                    return True

            return False

        return not dfs(0, -1) and n == len(visited)
        