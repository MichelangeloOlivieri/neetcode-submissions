class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        res = 1
        for i, (x, y) in enumerate(points):
            counts = {}
            for xx, yy in points[i + 1: ]:
                dx, dy = xx - x, yy - y
                g = self.gcd(dx, dy)
                dx, dy = dx // g, dy // g
                if dx < 0 or (dx == 0 and dy < 0): 
                    dx, dy = -dx, -dy
                key = (dx, dy)
                counts[key] = counts.get(key, 0) + 1
                res = max(res, counts[key] + 1)
        return res

    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

        """
        - Time complexity O(n**2), where n = len(points)
        - Space complexity O(n)
        """


        