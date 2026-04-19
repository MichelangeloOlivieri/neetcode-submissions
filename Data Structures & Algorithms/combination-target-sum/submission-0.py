class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        1) Empty input; example: nums = [5, 2, 3], target = 10 -> 4 combinations
        2) - Solution 1: a brute force approach might be done with a dfs on a binary
        tree
        """

        # edge cases
        if not nums or not target:
            return None

        # dfs implementation
        res = []
        combination = []
        inserted_combs = set()

        def dfs(target):

            if target == 0:
                comb_tuple = tuple(sorted(combination))
                if comb_tuple not in inserted_combs:
                    inserted_combs.add(comb_tuple)
                    res.append(list(comb_tuple))
                return

            if target < 0:
                return

            for n in nums:
                combination.append(n)
                dfs(target - n)
                combination.pop()

        dfs(target)
        return res

        """
        3) Syntax and dry run: ok
        4) Time complexity O(2^n); space complexity O(n^2)
        """

