class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        """
        1) Empty inputs; assuming there are no prerequisites not already in the 
        courses list; example: numCourses = 3, prerequisites = [[0, 1], [1, 2]] ->
        True; prerequisites [[0, 1], [1, 0], [2, 1]] -> False
        2) The problem can be seen as an oriented graph where the nodes are the courses 
        themselves and the edges are given by the prerequisites; the answer is True
        if there are no cycles and False otherwise; so one can create the corresponding
        graph and then 
        """

        if not numCourses:
            return True
        if not prerequisites: 
            return True

        n = numCourses
        m = len(prerequisites)

        graph = {}
        for i in range(n):
            if i not in graph:
                graph[i] = []
        
        for i in range(m):
            graph[prerequisites[i][0]].append(prerequisites[i][1])

        visited = set()   
        visiting = set()

        def dfs(i):
            if i in visiting:
                return True
            if not graph[i] or i in visited:
                return
                
            visiting.add(i)
            for vicino in graph[i]:
                if dfs(vicino):
                    return True 

            visiting.remove(i)
            visited.add(i)
            
            return False

        for i in range(n):
            if dfs(i):
                return False
        
        return True

        """
        3) Syntax and dry run: ok
        4) Time complexity O(m + n); space complexity O(n)
        """


        