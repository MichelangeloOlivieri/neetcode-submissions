class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        # Dijkstra algorithm

        n = len(grid)
        if n == 1:
            return grid[0][0]

        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while min_heap:
            max_height, i, j = heapq.heappop(min_heap)

            if (i, j) in visited:
                continue

            if i == n - 1 and j == n - 1:
                return max_height

            visited.add((i, j))

            for dr, dc in directions:
                if (i + dr in range(n) 
                and j + dc in range(n)
                and (i + dr, j + dc) not in visited):
                    new_max_height = max(max_height, grid[i + dr][j + dc])
                    heapq.heappush(min_heap, (new_max_height, i + dr, j + dc))

        return 0

        """
        Time complexity O(n^2 * log(n)), where n = len(grid); space complexity O(n^2)
        """