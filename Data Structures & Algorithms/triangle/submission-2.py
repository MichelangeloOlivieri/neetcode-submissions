class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        if not triangle or not triangle[0]:
            return 0

        h = len(triangle)

        for i in range(h - 2, -1, -1):
            for j in range(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])

        return triangle[0][0]
        
        """
        - Time complexity O(h**2), where h = len(triangle)
        - Space complexity O(1)
        """