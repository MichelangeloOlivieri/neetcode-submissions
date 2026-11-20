class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = collections.defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        min_heap = [(0, k)]
        visited = set()
        res = 0

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if node in visited:
                continue

            visited.add(node)
            res = max(res, time)

            for nei, weight in graph[node]:
                if nei not in visited:
                    heapq.heappush(min_heap, (time + weight, nei))
            
        return res if len(visited) == n else -1

"""
- Time complexity: O(E * log(E)), where E = len(times).
- Space complexity O(E + n).
"""