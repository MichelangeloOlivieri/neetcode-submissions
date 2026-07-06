import heapq

class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        # ==========================================
        # Clarifying Questions:
        # 1. Are tasks pre-sorted by start time? (No, must sort).
        # 2. What happens during CPU idle time? (Time jumps directly to the next task's start time).
        # 3. Can multiple tasks have identical start and processing times? (Yes, break ties with original index).
        #
        # Algorithm Description:
        # Sort tasks by start time while preserving original indices, then simulate time progression using a Min-Heap to dynamically execute the shortest available task.
        # ==========================================

        if not tasks:
            return []

        indexed_tasks = [
            (start, process, idx) for idx, (start, process) in enumerate(tasks)
        ]
        
        indexed_tasks.sort(key=lambda x: x[0])

        res = []
        min_heap = []
        
        i = 0
        current_time = 0
        n = len(indexed_tasks)

        while i < n or min_heap:
            if not min_heap and current_time < indexed_tasks[i][0]:
                current_time = indexed_tasks[i][0]

            while i < n and indexed_tasks[i][0] <= current_time:
                _, process, original_idx = indexed_tasks[i]
                heapq.heappush(min_heap, (process, original_idx))
                i += 1

            process_time, original_idx = heapq.heappop(min_heap)
            current_time += process_time
            res.append(original_idx)

        return res

        # ==========================================
        # Time Complexity: O(N log N)
        # Space Complexity: O(N)
        # ==========================================