from collections import defaultdict
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        # post-order dfs solution
        
        graph = defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
            
        for u in graph:
            graph[u].sort(reverse=True)
            
        res = []
        
        def dfs(airport):
            while graph[airport]:
                next_dest = graph[airport].pop()
                dfs(next_dest)

            res.append(airport)
            
        dfs("JFK")
        
        return res[::-1]

        """
        Time complexity O(E * log(E)); space complexity O(V + E)
        """