class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        sorted_queries = sorted([(q, i) for i, q in enumerate(queries)])

        min_heap = []
        res = [-1] * len(queries)
        i = 0

        for q, original_index in sorted_queries:

            # saving active intervals
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                size = r - l + 1
                heapq.heappush(min_heap, (size, r))
                i += 1
            
            # discarding espired intervals
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            if min_heap:
                res[original_index] = min_heap[0][0]

        return res

        """
        Time complexity O(mlog(m) + nlog(n)); space complexity O(m + n)
        """
