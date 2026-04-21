class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        """
        1) No empty input; suppose heights[i] >= 0 for each i
        2) - Solution 1: use two indexes and get O(n^2) time
        - Solution 2: use a stack
        """

        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area 

