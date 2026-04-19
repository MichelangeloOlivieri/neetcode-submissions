class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        """
        1) Empty inputs
        2) Precede as before running a dfs on any node to determine the presence of 
        loops and if the graph is connected
        """

        # edge cases

        if not n:
            return True
        if len(edges) != n - 1: # a tree (acyclic connected graph) with n nodes always has n - 1 edges
            return False

        # dfs implementation

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
                if nei == parent:
                    continue
                if dfs(nei, i):
                    return True

            return False
        
        if dfs(0, -1):
            return False
        
        return n == len(visited)

        """
        3) Syntax and dry run: ok
        4) Time complexity O(V); space complexity O(E)
        """



        