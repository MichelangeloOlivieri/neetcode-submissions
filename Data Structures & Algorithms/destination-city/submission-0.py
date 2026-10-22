class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        if not paths or not paths[0]:
            return ""

        graph = {}
        for u, v in paths:
            graph[u] = v

        node = paths[0][1]
        while node in graph:
            node = graph[node]

        return node

        """
        - Time complexity O(V), where V = #{cities}
        - Space complexity O(V)
        """