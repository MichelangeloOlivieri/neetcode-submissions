class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if not edges:
            return [0]

        degree = [0] * n

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([i for i in range(n) if degree[i] == 1])
        remaining_nodes = n

        while remaining_nodes > 2:      # mathematical fact
            leaves_count = len(leaves)

            for i in range(leaves_count):
                leaf = leaves.popleft()
                for nei in graph[leaf]:
                    degree[nei] -= 1
                    if degree[nei] == 1:
                        leaves.append(nei)

            remaining_nodes -= leaves_count

        return list(leaves)

        """
        - Time complexity O(n), where n = #{nodes}
        - Space complexity O(n)
        """