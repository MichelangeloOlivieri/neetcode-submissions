class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:

        m = len(heights)
        n = len(heights[0])
        min_effort = [[float('inf')] * n for _ in range(m)]
        min_effort[0][0] = 0
        min_heap = [[0, 0, 0]]
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            if r == m - 1 and c == n - 1:
                return effort

            if effort > min_effort[r][c]:
                continue

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if new_r in range(m) and new_c in range(n):
                    jump_effort = abs(heights[r][c] - heights[new_r][new_c])
                    new_max_effort = max(effort, jump_effort) 

                    if new_max_effort < min_effort[new_r][new_c]:
                        min_effort[new_r][new_c] = new_max_effort
                        heapq.heappush(min_heap, [new_max_effort, new_r, new_c])

        return 0

        """
        Time complexity O(m * n * log(m * n)); space complexity O(m * n)
        """