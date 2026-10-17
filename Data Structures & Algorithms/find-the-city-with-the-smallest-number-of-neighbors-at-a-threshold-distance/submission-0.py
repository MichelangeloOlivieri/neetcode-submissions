class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = (float('inf'), float('inf'))
       
        for i in range(n):
            min_heap = [(0, i)]
            min_weight = [float('inf')] * n
            min_weight[i] = 0
            reachable = {j : 0 for j in range(n)}

            while min_heap:
                weight, node = heapq.heappop(min_heap)

                if weight > min_weight[node]:
                    continue
                elif weight <= distanceThreshold:
                    reachable[node] = 1

                for nei, w in graph[node]:
                    new_weight = weight + w
                    if new_weight < min_weight[nei]:
                        min_weight[nei] = new_weight
                        heapq.heappush(min_heap, (new_weight, nei))

            cities_count = sum(reachable[j] for j in reachable) - 1
            if cities_count < res[0] or (cities_count == res[0] and i > res[1]):
                res = (cities_count, i)

        return res[1]

        """
        - Time complexity O(V * E * log(E)), where V = n and E = len(edges)
        - Space complexity O(V + E)
        """