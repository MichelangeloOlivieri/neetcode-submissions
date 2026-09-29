class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        res = []

        def backtrack(i, curr):
            if len(curr) == k:
                res.append(list(curr))
                return
            if len(curr) + n - i + 1 < k:
                return

            curr.append(i)
            backtrack(i + 1, curr)
            curr.pop()
            backtrack(i + 1, curr)

        backtrack(1, [])
        return res

        """
        -- Time complexity O(k * (n k))
        -- Space complexity O(k)
        """