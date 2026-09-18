class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:

        if not tasks:
            return []

        indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        indexed_tasks.sort(key=lambda x: x[0])

        res = []
        min_heap = []
        current_time = 0
        i = 0
        n = len(indexed_tasks)

        while i < n or min_heap:
            if not min_heap and current_time < indexed_tasks[i][0]:
                current_time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= current_time:
                _, process_time, index = indexed_tasks[i]
                heapq.heappush(min_heap, (process_time, index))
                i += 1

            process_time, index = heapq.heappop(min_heap)
            current_time += process_time
            res.append(index)

        return res

        """
        - Time complexity O(n * log(n)), where n = len(tasks)
        - Space complexity O(n)
        """