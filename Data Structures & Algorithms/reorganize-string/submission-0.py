class Solution:
    def reorganizeString(self, s: str) -> str:

        """
        1) s = "aabb" -> "abab"; s = "aa" -> ""
        2) Max Heap
        """

        res = []
        freq = defaultdict(int)
        for c in s:
            freq[c] += 1

        max_heap = []
        for c in freq:
            heapq.heappush(max_heap, (-freq[c], c))

        while max_heap:
            count1, c1 = heapq.heappop(max_heap)
            count1 = -count1
            if res and res[-1] == c1:
                if max_heap:
                    count2, c2 = heapq.heappop(max_heap)
                    count2 = -count2
                    res.append(c2)
                    count2 -= 1
                    if count2 > 0:
                        heapq.heappush(max_heap, (-count2, c2))
                    heapq.heappush(max_heap, (-count1, c1))
                else:
                    return ""
            else:
                res.append(c1)
                count1 -= 1
                if count1 > 0:
                    heapq.heappush(max_heap, (-count1, c1))

        return "".join(res)

        """
        - s = "ababccdac"
        - freq = {a : 3, b : 2, c : 3, d : 1}
        - max_heap = [(3, a), (3, c), (2, b), (1, d)]
        - res = []

        """

        """
        - Time complexity O(n * log(n)), where n = len(s)
        - Space complexity O(n)
        """