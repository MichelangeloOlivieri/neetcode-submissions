class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        if len(profits) != len(capital):
            return -1
        
        projects = sorted(zip(capital, profits))
        max_heap = []
        n = len(projects)
        i = 0

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w

        """
        - Time complexity O(n * log(n)), where n = len(profits)
        - Space complexity O(n)
        """