class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = -1
        min_reachable = float('inf')
       
        for i in range(n):
            min_heap = [(0, i)]
            min_weight = [float('inf')] * n
            min_weight[i] = 0

            while min_heap:
                weight, node = heapq.heappop(min_heap)

                if weight > min_weight[node]:
                    continue

                for nei, w in graph[node]:
                    new_weight = weight + w
                    if new_weight < min_weight[nei]:
                        min_weight[nei] = new_weight
                        heapq.heappush(min_heap, (new_weight, nei))

            count = sum(1 for w in min_weight if w <= distanceThreshold) - 1
            if count <= min_reachable:
                min_reachable = count
                res = i

        return res

        """
        - Time complexity O(V * E * log(E)), where V = n and E = len(edges)
        - Space complexity O(V + E)
        """