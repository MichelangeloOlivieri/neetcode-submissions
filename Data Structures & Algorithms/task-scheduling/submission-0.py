class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        """
        1) No empty input; example on paper
        2) Find the most frequent tasks; use a heap to order based on frequency
        """

        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1

            if max_heap:
                cnt = heapq.heappop(max_heap) + 1
                if cnt != 0:
                    q.append([cnt, time + n])

            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(max_heap, cnt)

        return time

        """
        3) Ok
        4) Time complexity O(n), where n = len(tasks), space complexity O(n)
        """