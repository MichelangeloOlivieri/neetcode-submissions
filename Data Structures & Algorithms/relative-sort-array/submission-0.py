class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        """
        1) arr1 = [1, 3, 6, 3, 4], arr2 = [1, 4, 3] -> [1, 4, 3, 3, 6]
        2) Count frequency of elements in arr1 for those in arr2, and the others put them into a heap
        """

        if not arr1:
            return []
        if not arr2:
            return sorted(arr1)

        nums = set(arr2)
        freq = defaultdict(int)
        min_heap = []

        for n in arr1:
            if n in nums:
                freq[n] += 1
            else:
                heapq.heappush(min_heap, n)

        res = []

        for n in arr2:
            while freq[n]:
                res.append(n)
                freq[n] -= 1

        while min_heap:
            res.append(heapq.heappop(min_heap))

        return res

        """
        - Time complexity O(m * log(m) + n), where m = len(arr1), n = len(arr2)
        - Space complexity O(m + n)
        """