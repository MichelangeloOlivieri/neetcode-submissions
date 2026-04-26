class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        """
        1) Example on paper
        2) Dfs
        """

        res = []

        def dfs(cur, remaining):
            if not remaining:
                res.append(cur.copy())
                return

            for n in remaining.copy():
                cur.append(n)
                remaining.remove(n)
                dfs(cur, remaining)
                remaining.add(cur.pop())

        dfs([], set(nums))
        return res

        """
        3) On paper
        4) Time complexity O(n! * n); space complexity O(n)
        """