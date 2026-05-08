class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        """
        1) Empty input
        2) It is a graph problem
        """
        
        graph = collections.defaultdict(list)
        for i, nei in prerequisites:
            graph[i].append(nei)

        res = []
        visited = set()
        visiting = set()

        def dfs(i):
            if i in visiting:
                return True
            if i in visited:
                return 

            visiting.add(i)
            for nei in graph[i]:
                if dfs(nei):
                    return True
            
            visiting.remove(i)
            visited.add(i)
            res.append(i)

        for n in range(numCourses):
            if dfs(n):
                return []

        return res

        """
        3) Ok
        4) Time complexity O(numCourses); space complexity O(numCourses)
        """

        
        