class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        w = 3 * n
        blocked = [[False] * w for _ in range(w)]
        for r, row in enumerate(grid):
            for c, ch in enumerate(row):
                if ch != " ":
                    for k in range(3):
                        blocked[3 * r + k][3 * c + (2 - k if ch == "/" else k)] = True
        answer = 0
        for r in range(w):
            for c in range(w):
                if blocked[r][c]:
                    continue
                answer += 1
                blocked[r][c] = True
                stack = [(r, c)]
                while stack:
                    a, b = stack.pop()
                    for rr, cc in ((a - 1, b), (a + 1, b), (a, b - 1), (a, b + 1)):
                        if 0 <= rr < w and 0 <= cc < w and not blocked[rr][cc]:
                            blocked[rr][cc] = True
                            stack.append((rr, cc))
        return answer
