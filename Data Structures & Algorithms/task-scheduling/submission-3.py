class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        freq = defaultdict(int)
        for t in tasks:
            freq[t] += 1
        
        max_heap = [] # (frequency, task)
        q = deque() # (cooldown, frequency, task)
        count = 0

        for t in freq:
            heapq.heappush(max_heap, (-freq[t], t))

        while max_heap or q:
            # put available tasks into the heap
            while q and q[0][0] < count:
                _, frequency, task = q.popleft()
                heapq.heappush(max_heap, (frequency, task))

            # process the most frequent task
            if max_heap:
                frequency, task = heapq.heappop(max_heap)
                frequency += 1
                # put the task in the queue to be processed later
                if frequency < 0:
                    q.append((count + n, frequency, task))
            else:
                count = q[0][0]

            count += 1

        return count

"""
- Time complexity: O(m * log(m)), where m = len(tasks).
- Space complexity: O(m).
"""