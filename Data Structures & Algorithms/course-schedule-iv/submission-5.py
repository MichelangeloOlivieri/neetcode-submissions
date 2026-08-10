class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        if not queries:
            return []

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        memo = {}

        def dfs(node):
            if node in memo:
                return memo[node]

            reachable = set()
            for nei in graph[node]:
                reachable.add(nei)
                reachable |= dfs(nei)

            memo[node] = reachable
            return memo[node]

        for i in range(numCourses):
            dfs(i)

        return [queries[i][1] in memo[queries[i][0]] for i in range(len(queries))]

        """
        Time Complexity: O(V * (V + E) + Q), where V = numCourses, E = len(prerequisites) and Q = len(queries); space complexity O(V^2)
        """