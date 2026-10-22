class Solution:
    def destCity(self, paths: List[List[str]]) -> str:

        if not paths or not paths[0]:
            return ""

        graph = {}
        for u, v in paths:
            graph[u] = v

        for start in graph:
            end = graph[start]
            if end not in graph:
                return end

        return ""

        """
        - Time complexity O(V), where V = #{cities}
        - Space complexity O(V)
        """