class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        res = []
        n = len(tasks)

        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda x : x[0])
        min_heap = []
        time = 0
        i = 0

        while i < n or min_heap:
            # if no elements, reset the queue
            if not min_heap:
                time = max(time, tasks[i][0])
            # process the current queue (available tasks)
            while i < n and tasks[i][0] <= time:
                _, process_time, index = tasks[i]
                heapq.heappush(min_heap, (process_time, index))
                i += 1
            # process the shortest task
            process_time, index = heapq.heappop(min_heap)
            time += process_time
            res.append(index)

        return res

"""
- Time complexity: O(n * log(n)), where n = len(tasks).
- Space complexity: O(n).
"""