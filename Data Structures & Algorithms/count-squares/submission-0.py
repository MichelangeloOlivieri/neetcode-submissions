from collections import defaultdict
from typing import List

class CountSquares:
    def __init__(self):
        self.pts_map = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.pts_map[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point

        for (x, y), freq in self.pts_map.items():
            if abs(px - x) != abs(py - y) or px == x or py == y:
                continue
            
            freq_corner1 = self.pts_map.get((x, py), 0)
            freq_corner2 = self.pts_map.get((px, y), 0)
            
            res += freq * freq_corner1 * freq_corner2

        return res