class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = [] # (rectangle_start, height)

        for curr_right, h in enumerate(heights):
            curr_left = curr_right
            while stack and stack[-1][1] > h:
                prev_left, height = stack.pop()
                max_area = max(max_area, height * (curr_right - prev_left))
                curr_left = prev_left
            stack.append((curr_left, h))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area

"""
- Time complexity: O(n), where n = len(heights).
- Space complexity: O(1).
"""