from collections import deque
from typing import List

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:

        def topo_sort(edges: List[List[int]]) -> List[int]:
            graph = [[] for _ in range(k + 1)]
            in_degree = [0] * (k + 1)
            
            for u, v in edges:
                graph[u].append(v)
                in_degree[v] += 1
                
            q = deque([i for i in range(1, k + 1) if in_degree[i] == 0])
            order = []
            
            while q:
                node = q.popleft()
                order.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
                        
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        if not row_order:
            return []
            
        col_order = topo_sort(colConditions)
        if not col_order:
            return []

        row_pos = {val: i for i, val in enumerate(row_order)}
        col_pos = {val: j for j, val in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for val in range(1, k + 1):
            r = row_pos[val]
            c = col_pos[val]
            matrix[r][c] = val

        return matrix

        """
        - Time complexity O(k^2 + E + V)
        - Space complexity O(k^2 + E + V)
        """