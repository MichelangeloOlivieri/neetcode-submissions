class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        """
        1) nums = [1, 2, 2] -> [[1, 2, 2], [2, 1, 2], [2, 2, 1]]
        2) Array, Backtracking
        """

        if not nums:
            return []

        res = []
        visited = set()
        taken = set()

        def backtrack(curr):
            if tuple(curr) in taken:
                return
            if len(curr) == len(nums):
                taken.add(tuple(curr))
                res.append(list(curr))

            for i in range(len(nums)):
                if i not in visited:
                    visited.add(i)
                    curr.append(nums[i])
                    backtrack(curr)
                    curr.pop()
                    visited.remove(i)
        
        backtrack([])
        return res

        """
        3) nums = [1, 2, 2]
        - i = 0: visited = {0}, curr = [1] -> i = 0: NO
                                           -> i = 1: visited = {0, 1}, curr = [1, 2] -> i = 0: NO
-> i = 1: NO
-> i = 2: visited = {0, 1, 2}, curr = [1, 2, 2] -> taken = {(1, 2, 2)}, res = [[1, 2, 2]]
                                           -> i = 2: visited = {0, 2}, curr = [1, 2] -> i = 0: N0
-> i = 1: visited = {0, 2, 1}, curr = [1, 2, 2] -> NO
-> i = 2: NO
        - i = 1: visited = {1}, curr = [2], ...
        4) Time complexity O(n!), where n = len(nums); space complexity O(n!)
        """  