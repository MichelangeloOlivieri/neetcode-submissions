class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]
        rank = [1] * n

        def find(u):
            if u != parent[u]:
                u = find(parent[u])
            return u

        def union(u, v):
            p = find(u)
            q = find(v)

            if p == q:
                return 0

            if rank[p] > rank[q]:
                parent[q] = p
            elif rank[q] > rank[p]:
                parent[p] = q
            else:
                parent[q] = p
                rank[p] += 1

            return 1

        m = n
        for u, v in edges:
            m -= union(u, v)

        return m == 1
        