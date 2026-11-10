from collections import defaultdict

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        """
        1) - (x, y) = (2, 3) 
        -> horizontal = {2 : 1}, vertical = {3 : 1}, diagonal = {}
        - (x, y) = (5, 5) 
        -> ..., diagonal = {(2/3, 7/3) : 1}

        horizontal: y = k
        vertical: x = k
        diagonal: y = mx + q

        3 = 2m + q
        5 = 3m + q
        -> 2 = 3m -> m = 2/3 -> q = 7/3
        """

        if not points:
            return 0

        horizontal = defaultdict(int)
        vertical = defaultdict(int)
        diagonal = {}
        n = len(points)

        for i in range(n):
            x, y = points[i]
            horizontal[y] += 1
            vertical[x] += 1
            seen = set()
            for j in range(0, i):
                a, b = points[j]
                if a == x: 
                    continue
                m = (b - y) / (a - x)
                q = y - m * x
                if (m, q) in seen:
                    continue
                seen.add((m, q))
                if (m, q) not in diagonal:
                    diagonal[(m, q)] = 2
                else:
                    diagonal[(m, q)] += 1

        res = 0
        for y in horizontal:
            res = max(res, horizontal[y])
        for x in vertical:
            res = max(res, vertical[x])
        for t in diagonal:
            res = max(res, diagonal[t])

        return res

        """
        - Time complexity O(n**2), where n = len(points)
        - Space complexity O(n)
        """


        