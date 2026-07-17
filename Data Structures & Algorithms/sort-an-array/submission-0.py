class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        """
        1) nums = [1, 3, 2, 1] -> [1, 1, 2, 3]
        2) 
        """

        if not nums:
            return [] 

        res = []
        heapq.heapify(nums) # O(nlog(n))

        while nums:
            n = heapq.heappop(nums)
            res.append(n)

        return res 

    def heapify(self, arr: list[int]) -> None:
        pass
        