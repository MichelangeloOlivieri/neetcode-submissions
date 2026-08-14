class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        """
        1) prerequisites = [[0, 1], [1, 2] [0, 2]], queries = [[0, 1], [0, 2]] -> [True, True]
        2) DP, Tree problem
        """
        
        if not queries:
            return []

        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[u].append(v)

        res = [False] * len(queries)
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

        for i in range(len(queries)):
            if queries[i][1] in memo[queries[i][0]]:
                res[i] = True

        return res