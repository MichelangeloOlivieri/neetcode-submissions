class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        """
        1) No empty input; uniqueness not guaranteed; assuming k >= 0
        2) For each point calculate the distance from the origin, and create a heap
        whose values are the distances but can also keep track of the indexes
        """

        distances = []
        res = []

        for x, y in points:
            d = x**2 + y**2
            distances.append([d, x, y])

        heapq.heapify(distances)

        for _ in range(k):
            d, x, y = heapq.heappop(distances)
            res.append([x, y])

        return res

        """
        3) Ok
        4) Time complexity O(n + klog(n)), where n = len(points); space complexity 
        O(n)
        """ 