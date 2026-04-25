class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        """
        1) No empty input; not counting order
        2) Dfs
        """

        res = []
        cur = []

        def dfs(i):
            if i == len(nums):
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()
            dfs(i + 1)

        dfs(0)
        return res

        """
        3) Ok
        4) Time complexity O(n * 2^n), space complexity O(n)
        """
            
            