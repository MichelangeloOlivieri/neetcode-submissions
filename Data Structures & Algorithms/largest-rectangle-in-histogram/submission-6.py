class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = [] # (rectangle_start, height)

        for r, h in enumerate(heights):
            l = r
            while stack and stack[-1][1] > h:
                left_index, height = stack.pop()
                max_area = max(max_area, height * (r - left_index))
                l = left_index
            stack.append((l, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

"""
- Time complexity: O(n), where n = len(heights).
- Space complexity: O(1).
"""