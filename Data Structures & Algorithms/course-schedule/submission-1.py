class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        degree = [0] * numCourses
        
        for course, pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1
        
        queue = deque([i for i in range(numCourses) if degree[i] == 0])
        followed = 0
        
        while queue:
            curr = queue.popleft()
            followed += 1
            for neighbor in graph[curr]:
                degree[neighbor] -= 1
                if degree[neighbor] == 0:
                    queue.append(neighbor)
        
        return followed == numCourses

        """
        - Time complexity O(E + V), where E = numCourses and V = len(prerequisites)
        - Space complexity O(E + V)
        """