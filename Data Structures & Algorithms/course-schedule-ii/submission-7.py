class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        if not prerequisites:
            return [i for i in range(numCourses)]

        graph = defaultdict(list)
        degree = [0] * numCourses

        for u, v in prerequisites:
            graph[v].append(u)  
            degree[u] += 1

        q = deque([i for i in range(numCourses) if degree[i] == 0])
        res = []

        while q:
            node = q.popleft()
            res.append(node)

            for nei in graph[node]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    q.append(nei)

        return res if len(res) == numCourses else []

        """
        - Time complexity O(E + V), where E = len(prerequisites) and V = numCourses
        - Space complexity O(E + V)
        """     