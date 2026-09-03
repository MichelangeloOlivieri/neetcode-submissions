class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
        self.count = n

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

        self.count -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:

        if not nums:
            return False

        if len(nums) == 1:
            return True

        uf = UnionFind(len(nums))
        factor_index = {}

        for i, n in enumerate(nums):

            if n == 1:
                return False

            f = 2
            while f * f <= n:
                if n % f == 0:
                    if f in factor_index:
                        uf.union(factor_index[f], i)
                    else:
                        factor_index[f] = i

                    while n % f == 0:
                        n //= f
                f += 1

            if n > 1:
                if n in factor_index:
                    uf.union(factor_index[n], i)
                else:
                    factor_index[n] = i

        return uf.count == 1

        """
        - Time complexity O(M * sqrt(N)), where M = len(nums) and N = max(nums)
        - Space complexity O(M + N) 
        """        