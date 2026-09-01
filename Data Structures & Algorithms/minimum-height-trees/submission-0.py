class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        while u != self.par[u]:
            self.par[u] = self.par[self.par[u]]
            u = self.par[u]
        return u

    def union(self, u, v):
        p = self.find(u)
        q = self.find(v)

        if p == q:
            return False

        if self.rank[p] > self.rank[q]:
            self.par[q] = p
        elif self.rank[p] < self.rank[q]:
            self.par[p] = q
        else:
            self.par[q] = p
            self.rank[p] += 1

        return True

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        """
        1) n = 3, edges = [[1, 2], [2, 3], [2, 4]] -> [2]
        2) Tree, Union Find
        """

        res = []

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()

        def dfs(u):
            visited.add(u)

            height = 1
            for nei in graph[u]:
                if nei not in visited:
                    height = max(height, 1 + dfs(nei))

            visited.remove(u)
            return height

        min_height = float('inf')
        for i in range(n):
            height = dfs(i)
            if height <= min_height:
                min_height = height
                while res and res[-1][1] > height:
                    res.pop()
                res.append([i, height])

        return [i for i, height in res]

        """
        - graph = {0 : [1], 1 : [0, 2, 3], 2 : [1], 3 : [1]}
        - min_height = float('inf')
        - i = 0: height = 3, min_height = 3
        """        