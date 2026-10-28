class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        if not items or not items[0]:
            return [0] * len(queries)
        if not queries:
            return []
        
        n = len(items)
        items.sort()
        res = []

        for i in range(1, len(items)):
            items[i][1] = max(items[i][1], items[i - 1][1])

        for offer in queries:
            beauty = 0
            l = 0
            r = n - 1
            index = 0

            while l <= r:
                mid = l + (r - l) // 2
                if items[mid][0] == offer:
                    beauty = max(beauty, items[mid][1])
                    index = max(index, mid)
                    break
                elif offer > items[mid][0]:
                    beauty = max(beauty, items[mid][1])
                    index = max(index, l)
                    l = mid + 1
                else:
                    r = mid - 1

            while index < n and items[index][0] <= offer:
                beauty = max(beauty, items[index][1])
                index += 1

            res.append(beauty)

        return res

        """
        - Time complexity O((m + n) * log(n)), where n = len(items) and m = len(queries)
        - Space complexity O(m + n) (for TimSort and result)
        """