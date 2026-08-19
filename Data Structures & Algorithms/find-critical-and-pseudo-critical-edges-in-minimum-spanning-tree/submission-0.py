class UnionFind:
    def __init__(self, n: int) -> None:
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u: int) -> int:
        while u != self.par[u]:
            self.par[u] = self.par[self.par[u]]
            u = self.par[u]
        return u

    def union(self, u: int, v: int) -> bool:
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
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        
        if not edges:
            return []

        for i in range(len(edges)):
            edges[i].append(i)

        edges.sort(key=lambda e: e[2])

        uf_base = UnionFind(n)
        base_weight = 0
        for u, v, w, i in edges:
            if uf_base.union(u, v):
                base_weight += w

        critical = []
        pseudo = []

        for u, v, w, i in edges:

            uf_ignore = UnionFind(n)
            ignore_weight = 0
            used_edges = 0
            for u2, v2, w2, i2 in edges:
                if i != i2 and uf_ignore.union(u2, v2):
                    ignore_weight += w2
                    used_edges += 1

            if ignore_weight > base_weight or used_edges != n - 1:
                critical.append(i)
                continue

            uf_force = UnionFind(n)
            uf_force.union(u, v)
            force_weight = w
            for u2, v2, w2, i2 in edges:
                if uf_force.union(u2, v2):
                    force_weight += w2

            if force_weight == base_weight:
                pseudo.append(i)

        return [critical, pseudo]