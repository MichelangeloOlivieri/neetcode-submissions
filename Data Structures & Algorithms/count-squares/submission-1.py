class CountSquares:
    def __init__(self):
        self.freq = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.freq[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        curr_x, curr_y = point

        for (x, y), freq in self.freq.items():
            if abs(curr_x - x) != abs(curr_y - y) or curr_x == x or curr_y == y:
                continue
            
            first_corner_freq = self.freq.get((x, curr_y), 0) # avoids changing size during iteration!
            second_corner_freq = self.freq.get((curr_x, y), 0)
            
            res += freq * first_corner_freq * second_corner_freq

        return res

        """
        - Time complexity O(n), where n = #{unique streamed points}
        - Space complexity O(n)
        """