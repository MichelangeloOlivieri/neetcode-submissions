class Solution:
    def trap(self, height: List[int]) -> int:

        if not height:
            return 0

        n = len(height)
        max_left = [0] * n
        max_right = [0] * n
        max_left[0] = height[0]
        max_right[n - 1] = height[n - 1]
        res = 0

        for i in range(1, n):
            max_left[i] = max(height[i], max_left[i - 1])

        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])

        for i in range(n):
            res += max(min(max_left[i], max_right[i]) - height[i], 0)

        return res

        """
        Time complexity O(n); space complexity O(n)
        """