class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)
        for i, eq in enumerate(equations):
            u, v = eq
            graph[u].append([v, values[i]])
            graph[v].append([u, 1 / values[i]])

        def bfs(i, target):
            if i not in graph or target not in graph:
                return -1

            q = deque()
            visited = set()
            q.append([i, 1])
            visited.add(i)

            while q:
                node, weight = q.popleft()
                if node == target:
                    return weight
                for nei, value in graph[node]:
                    if nei not in visited:
                        q.append([nei, weight * value])
                        visited.add(nei)

            return -1

        return [bfs(q[0], q[1]) for q in queries]

        """
        - Time complexity O(E + V), where E = #{unique variables} and V = len(equations)
        - Space complexity O(E + V) 
        """