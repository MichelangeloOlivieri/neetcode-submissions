class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))
        
        min_heap = [(0, k)]
        min_cost = {i : float('inf') for i in range(1, n + 1)}
        min_cost[k] = 0
        visited = set()

        while min_heap:
            time, node = heapq.heappop(min_heap)

            if time > min_cost[node]:
                continue

            visited.add(node)
            if len(visited) == n:
                return time

            for nei, cost in graph[node]:
                new_time = time + cost
                if new_time < min_cost[nei]:
                    min_cost[nei] = new_time
                    heapq.heappush(min_heap, (new_time, nei))

        return -1

        