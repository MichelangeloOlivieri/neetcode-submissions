class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        """
        1) Input is guaranteed nonempty, so no worries; example: n = 3, nums = [1, 2,
        3, 1], return 1
        2) - First idea is to create a hash set and scan the array to stop when I find 
        the repeated number -> O(n) time and space
        - 
        """

        seen = set()
        for n in nums:
            if n in seen:
                return n
            seen.add(n)
            
        