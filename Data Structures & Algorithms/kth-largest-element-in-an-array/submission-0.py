class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        """
        1) No empty input
        2) - Solution 1: sort the array and retrieve its k-th element (time 
        O(nlog(n)))
        - Solution 2: heapify and heappop (time should be O(n + klog(n)))
        """

        neg_nums = [-n for n in nums]
        heapq.heapify(neg_nums)
        
        count = 1
        while count < k:
            heapq.heappop(neg_nums)
            count += 1

        return -neg_nums[0]

        """
        3) Ok
        4) Time complexity O(n + klog(n)); space complexity O(n)
        """
        
