class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        """
        1) Empty input; assuming only integers greater than 0; example on paper
        2) Use heap data structure to heapify and destroy the stones until 
        len(stones) <= 1
        """

        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]

        neg_stones = [-s for s in stones]
        heapq.heapify(neg_stones)

        while len(neg_stones) > 1:

            stone1 = heapq.heappop(neg_stones)
            stone2 = heapq.heappop(neg_stones)

            if stone1 != stone2:
                heapq.heappush(neg_stones, stone1 - stone2)

        if not neg_stones:
            return 0
        if len(neg_stones) == 1:
            return -neg_stones[0]

        """
        3) Ok
        4) Time complexity O(nlog(n)), where n = len(stones); space complexity O(n)
        """
