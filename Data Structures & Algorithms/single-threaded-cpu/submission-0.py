class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        """
        - no task to process -> idle
        - if there task -> shortest processing time, smallest index
        - process the task, then start another one
        """

        if not tasks:
            return []

        indexed_tasks = [(tasks[i][0], tasks[i][1], i) for i in range(len(tasks))]
        indexed_tasks.sort(key=lambda x : x[0])

        min_heap = []
        i = 0
        current_time = 1
        res = []
        n = len(tasks)

        while i < n or min_heap:
            if not min_heap and current_time < indexed_tasks[i][0]:
                current_time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= current_time:
                _, process, original_index = indexed_tasks[i]
                heapq.heappush(min_heap, (process, original_index))
                i += 1

            process_time, original_idx = heapq.heappop(min_heap)
            current_time += process_time
            res.append(original_idx)
        
        return res


        