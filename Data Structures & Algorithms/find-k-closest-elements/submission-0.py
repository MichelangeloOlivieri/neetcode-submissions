class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:

        """
        1) arr = [1, 4, 2, 7], k = 2, x = 5 -> [4, 7]
        2) max_heap to keep track of k least differences
        """        

        if not arr:
            return []

        if k >= len(arr):
            return arr

        max_heap = []
        res = []

        for i in range(len(arr)):
            diff = abs(x - arr[i])

            if len(max_heap) < k:
                heapq.heappush(max_heap, [-diff, arr[i]])

            elif (-diff > max_heap[0][0]) or (-diff == max_heap[0][0] and arr[i] < max_heap[0][1]):
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, [-diff, arr[i]])

        for i in range(len(max_heap)):
            res.append(max_heap[i][1])

        res.sort()
        return res

        """
        Time complexity O(n * log(n)), where n = len(arr); space complexity O(n)
        """       
