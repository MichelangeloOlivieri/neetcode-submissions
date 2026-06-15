class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        if not edges:
            return 0

        parent = [i for i in range(n)]
        rank = [1] * n
        res = n

        def find(u):
            while u != parent[u]:
                u = find(parent[u])
            return u

        def union(u, v):
            p = find(u)
            q = find(v)

            if p == q:
                return 0

            if rank[p] > rank[q]:
                parent[q] = p
            elif rank[p] < rank[q]:
                parent[p] = q
            else:
                parent[q] = p
                rank[p] += 1

            return 1

        for u, v in edges:
            res -= union(u, v)

        return res