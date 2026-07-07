class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        """
        - Use a array to keep track of incoming orders and a heap to choose the task;
        sort the tasks

        - tasks = [[1, 50], [2, 3], [1, 1], [1, 1]] -> [[1, 1], [1, 1], [1, 50], 
        [2, 3]]
        - indexed_tasks = [[1, 50, 0], [2, 3, 1], [1, 1, 2], [1, 1, 3]] ->
        -> [[1, 1, 2], [1, 1, 3], [1, 50, 0], [2, 3, 1]] (incoming tasks)

        - time = 0 -> time = 1; min_heap = [(1, 2)]
        -> i = 1; min_heap = [(1, 2), (1, 3)]
        -> i = 2; min_heap = [(1, 2), (1, 3), (50, 0)]
        -> i = 3; time = 1 < 2
        - process_time, index = 1, 2 -> time = 2
        -> i = 3; min_heap = [everything]
        """

        if not tasks:
            return []

        n = len(tasks)
        indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(n)]
        indexed_tasks.sort()
        min_heap = []
        time = 0
        i = 0
        res = []

        while i < n or min_heap:

            if not min_heap and time < indexed_tasks[i][0]:
                time = indexed_tasks[i][0]

            while i < n and time >= indexed_tasks[i][0]:
                _, process_time, index = indexed_tasks[i]
                heapq.heappush(min_heap, (process_time, index))
                i += 1

            process_time, index = heapq.heappop(min_heap)
            time += process_time
            res.append(index)

        return res

        """
        Time complexity O(n * log(n)); space complexity O(n)
        """


            
            