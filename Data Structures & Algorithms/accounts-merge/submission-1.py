class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u):
        while u != self.par[u]:
            u = self.par[self.par[u]]
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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        if not accounts or not accounts[0]:
            return [[]]

        uf = UnionFind(len(accounts))
        email_to_account = defaultdict(int)

        for i in range(len(accounts)):
            for j in range(1, len(accounts[i])):
                e = accounts[i][j]
                if e not in email_to_account:
                    email_to_account[e] = i
                else:
                    uf.union(i, email_to_account[e])

        email_group = defaultdict(list)

        for e in email_to_account:
            leader = uf.find(email_to_account[e])
            email_group[leader].append(e)

        res = []

        for i in email_group:
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))

        return res

        """
        Time complexity O(m * n * log(m * n); space complexity O(m * n)
        """ 