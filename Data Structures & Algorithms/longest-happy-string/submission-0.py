class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        max_heap = []
        for count, c in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(max_heap, (count, c))

        res = []

        while max_heap:
            count, c = heapq.heappop(max_heap)

            if len(res) >= 2 and res[-2] == res[-1] == c:
                if max_heap:
                    new_count, new_c = heapq.heappop(max_heap)

                    res.append(new_c)
                    new_count += 1
                    if new_count != 0:
                        heapq.heappush(max_heap, (new_count, new_c))

                    heapq.heappush(max_heap, (count, c))

            else:
                res.append(c)            
                count += 1
                if count != 0:
                    heapq.heappush(max_heap, (count, c))

        return "".join(res)

        """
        - Time complexity O(N), where N = a + b + c
        - Space complexity O(N)
        """