class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_area = 0
        stack = []

        for i, h in enumerate(heights):
            curr_left = i
            while stack and stack[-1][1] > h:
                left, height = stack.pop()
                max_area = max(max_area, height * (i - left))
                curr_left = left
            stack.append((curr_left, h))
        
        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area