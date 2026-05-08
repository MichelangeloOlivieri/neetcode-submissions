class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        """
        1) Empty input
        2) It is a graph problem
        """

        from typing import List
import collections

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = collections.defaultdict(list)
        for crs, pre in prerequisites:
            graph[crs].append(pre)

        res = []
        visited = set()
        visiting = set()

        def dfs(crs):
            if crs in visiting:
                return True
            if crs in visited:
                return 

            visiting.add(crs)
            for pre in graph[crs]:
                if dfs(pre):
                    return True
            
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)

        for c in range(numCourses):
            if dfs(c):
                return []

        return res

        """
        3) Ok
        4) Time complexity O(numCourses); space complexity O(numCourses)
        """

        
        