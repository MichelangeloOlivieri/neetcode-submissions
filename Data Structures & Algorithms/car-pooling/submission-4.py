class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        if not trips:
            return False

        trips.sort(key=lambda x: x[1])
        min_heap = []
        curr_pass = 0

        for t in trips:
            num_pass, start, end = t

            while min_heap and min_heap[0][0] <= start:
                curr_pass -= min_heap[0][1]
                heapq.heappop(min_heap)

            curr_pass += num_pass
            if curr_pass > capacity:
                return False
            
            heapq.heappush(min_heap, [end, num_pass])

        return True

        """
        Time complexity O(nlog(n))
        """