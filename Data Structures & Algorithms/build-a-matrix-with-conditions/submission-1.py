class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        """
        1) k = 2, rowConditions = [[3, 2], [2, 1], [3, 1]], colConditions = [[2, 1]]
        -> [[0, 2], 
            [1, 0]]
        2) Graph problem: process edges and assign row and column positions; if there is a cycle return empty list (conditions independent of each other)
        """

        row_graph = defaultdict(list)
        row_degree = defaultdict(int)
        for u, v in rowConditions:
            row_graph[u].append(v)
            row_degree[v] += 1

        row_q = deque([i for i in range(1, k + 1) if row_degree[i] == 0])
        row_values = []

        while row_q:
            node = row_q.popleft()
            row_values.append(node)
            for nei in row_graph[node]:
                row_degree[nei] -= 1
                if row_degree[nei] == 0:
                    row_q.append(nei)

        if len(row_values) != k:
            return []

        col_graph = defaultdict(list)
        col_degree = defaultdict(int)
        for u, v in colConditions:
            col_graph[u].append(v)
            col_degree[v] += 1

        col_q = deque([i for i in range(1, k + 1) if col_degree[i] == 0])
        col_values = []

        while col_q:
            node = col_q.popleft()
            col_values.append(node)
            for nei in col_graph[node]:
                col_degree[nei] -= 1
                if col_degree[nei] == 0:
                    col_q.append(nei)

        if len(col_values) != k:
            return []

        matrix = [[0] * k for _ in range(k)]

        coordinates = defaultdict(list)
        for i in range(len(row_values)):
            v = row_values[i]
            coordinates[v].append(i)
        for j in range(len(col_values)):
            v = col_values[j]
            coordinates[v].append(j)

        for v in coordinates:
            i = coordinates[v][0]
            j = coordinates[v][1]
            matrix[i][j] = v

        return matrix

        """
        - Time complexity O(E + V)
        - Space complexity O(E + V)
        """