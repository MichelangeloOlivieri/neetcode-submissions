class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        """
        1) No empty input; example on paper
        2) Dfs
        """

        nums.sort()
        res = []

        def dfs(i, cur):
            if i > len(nums) - 1:
                res.append(cur.copy())
                return

            cur.append(nums[i])
            dfs(i + 1, cur)
            cur.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1, cur)

        dfs(0, [])
        return res

        """
        3) Ok
        4) Time complexity O(n * 2^n), where n = len(nums); space complexity O(2^n)
        """