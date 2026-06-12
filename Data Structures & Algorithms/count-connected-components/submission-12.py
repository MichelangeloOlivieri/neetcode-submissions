class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        # union-find solution

        parent = [i for i in range(n)]
        rank = [1] * n
        res = n

        def find(u):
            if parent[u] != u:
                parent[u] = find(parent[u])
            return parent[u]

        def union(u, v):
            p1 = find(u)
            p2 = find(v)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                parent[p2] = p1
            elif rank[p2] > rank[p1]:
                parent[p1] = p2
            else:
                parent[p2] = p1
                rank[p1] += 1

            return 1

        for u, v in edges:
            res -= union(u, v)

        return res

        """
        Time complexity O(V + E); space complexity O(V)
        """
