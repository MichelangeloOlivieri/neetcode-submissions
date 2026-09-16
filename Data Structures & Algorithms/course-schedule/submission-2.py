class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        if not prerequisites: 
            return True

        m = numCourses
        n = len(prerequisites)

        graph = defaultdict(list)
        for i in range(n):
            if prerequisites[i]:
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

        for i in range(m):
            if dfs(i):
                return False
        
        return True

        """
        - Time complexity O(E + V), where E = numCourses and V = len(prerequisites)
        - Space complexity O(E + V)
        """        