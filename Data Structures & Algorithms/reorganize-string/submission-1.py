class Solution:
    def reorganizeString(self, s: str) -> str:

        res = []
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        max_heap = []
        for c in freq:
            heapq.heappush(max_heap, (-freq[c], c))

        while max_heap:
            count1, c1 = heapq.heappop(max_heap)
            if res and res[-1] == c1:
                if max_heap:
                    count2, c2 = heapq.heappop(max_heap)
                    res.append(c2)
                    count2 += 1
                    if count2 < 0:
                        heapq.heappush(max_heap, (count2, c2))
                    heapq.heappush(max_heap, (count1, c1))
                else:
                    return ""
            else:
                res.append(c1)
                count1 += 1
                if count1 < 0:
                    heapq.heappush(max_heap, (count1, c1))

        return "".join(res)

        """
        - Time complexity O(n * log(n)), where n = len(s)
        - Space complexity O(n)
        """