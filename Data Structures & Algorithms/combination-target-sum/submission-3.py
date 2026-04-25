class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        """
        1) Empty input; example: nums = [5, 2, 3], target = 10 -> 4 combinations
        2) - Solution 1: a brute force approach might be done with a dfs on a binary
        tree
        """

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])
            cur.pop()
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res

        """
        3) Syntax and dry run: ok
        4) Time complexity O(2^(target/min(nums) + len(nums))); space complexity 
        O(2^(target/min(nums)))
        """

