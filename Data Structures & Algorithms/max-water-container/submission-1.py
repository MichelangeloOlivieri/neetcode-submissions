class Solution:
    def maxArea(self, heights: List[int]) -> int:

        """
        1) heights = [2, 1, 3] -> 4
        2) Array, Two Pointers
        """

        if not heights:
            return 0

        l = 0
        r = len(heights) - 1
        res = 0

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)
            res = max(res, area)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return res

        """
        3) heights = [2, 1, 3]
        - l = 0, r = 2: area = 4, res = 4
        - l = 1, r = 2: area = 1, res = 4
        - l = 2, r = 2: break
        4) Time complexity O(n), where n = len(heights), space complexity O(1)
        """