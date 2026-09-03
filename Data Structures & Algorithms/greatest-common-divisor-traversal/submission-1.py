class UnionFind:
    def __init__(self, arr):
        self.par = arr
        self.rank = [1] * len(arr)

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
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        """
        1) nums = [3, 5, 15] -> True; nums = [3, 7, 14] -> False
        2) Union Find, Graph 
        """

        if not nums:
            return False

        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        graph = {}
        for i in range(len(nums)):
            graph[i] = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if gcd(nums[i], nums[j]) > 1:
                    graph[i].append(j)
                    graph[j].append(i)

        visited = set()

        def dfs(node):
            visited.add(node)
            for nei in graph[node]:
                if nei not in visited:
                    dfs(nei)

        dfs(0)
        return len(visited) == len(nums)

        """
        - nums = [4, 3, 12]
        - graph = {0 : [2], 1 : [2], 2 : [0, 1]}
        - dfs(0): visited = {0} -> dfs(2): visited = {0, 2} -> dfs(1): visited = {0, 2, 1}
        """