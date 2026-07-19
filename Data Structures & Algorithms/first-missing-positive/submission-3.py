class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        """
        1) Available options: greedy, two pointers
        2) Find max; initialize an array of length max (O(1) space for integer overflow) 
        with -float('inf') and fill it with numbers you find between 1 and max; return first
        index with -float('inf') 
        """

        if not nums:
            return 1 

        maximum = max(max(nums), 1)
        minimum = max(min(nums), 1)

        arr = [0] * maximum # O(1) for integer overflow
        if not arr:
            arr = [0]

        for n in nums:
            if n >= minimum:
                arr[n - 1] = 1

        for i in range(len(arr)):
            if arr[i] == 0:
                return i + 1

        return maximum + 1

        """
        3) nums = [-1, -2, -3]; maximum = 1, minimum = 1
        arr = [0]
        """
        
