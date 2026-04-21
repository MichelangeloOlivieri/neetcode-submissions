class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """
        1) No empty input; suppose heights[i] >= 0 for each i
        2) - Solution 1: use two indexes and get O(n^2) time
        - Solution 2
        """

        res = 0

        for i in range(len(heights)):
            lowest = heights[i]
            for j in range(i, len(heights)):
                lowest = min(lowest, heights[j])
                area = (j - i + 1) * lowest
                res = max(res, area)

        return res