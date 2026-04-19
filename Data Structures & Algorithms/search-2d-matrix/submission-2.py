class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # tentativo mio

        """
        1) Apart from edge cases (e.g. empty input) all is good
        2) It is clear that we have to implement a binary search in some way
        """
        up = 0
        down = len(matrix) - 1

        while up <= down:

            mid_y = (up + down) // 2
            left = 0
            right = len(matrix[0]) - 1

            while left <= right:
                mid_x = (left + right) // 2
                if matrix[mid_y][mid_x] == target:
                    return True
                elif matrix[mid_y][mid_x] < target:
                    left = mid_x + 1
                elif matrix[mid_y][mid_x] > target:
                    right = mid_x - 1

            if target > matrix[mid_y][-1]:
                up = mid_y + 1
            elif target < matrix[mid_y][0]:
                down = mid_y - 1
            else: 
                return False

        return False

        """
        3) Dry run: - [[2, 3, 4], [4, 5, 6]]; target = 2;
        - left = 0, right = 2, up = 0, down = 1, mid_y = 0, mid_x = 1;
        - matrix[0][1] = 3 > 2 = target, right = 0;
        - left = 0, right = 0, mid_x = 0, matrix[0][0] = 2 = target

        - [[2, 3, 4], [4, 5, 6]]; target = 7;
        - left = 0, right = 2, up = 0, down = 1, mid_y = 0, mid_x = 1;
        - matrix[0][1] = 3 < 7 = target, left = 2;
        - left = 2, right = 2, mid_x = 2, matrix[0][2] = 4 < 6 = target, left = 3;
        - left = 3, right = 2; left = 3 > 3 - 1 = 2; up = 1; down = 1;
        - left = 0, right = 2; mid_y = 1; mid_x = 1; matrix[1][1] = 5 < 7 = target;  

        - [[2, 3, 4], [4, 5, 6]]; target = 7;
        - left = 0, right = 2, up = 0, down = 1, mid_y = 0, mid_x = 1;
        - matrix[0][1] = 3 < 7 = target, left = 2;
        - left = 2, right = 2, mid_x = 2, matrix[0][2] = 4 < 7 = target, left = 3;
        - left = 3, right = 2; left = 3 > 3 - 1 = 2; up = 1; down = 1
        - left = 0, right = 2; mid_x = 1
        4) Time complexity O(log(m) * log(n)); space complexity O(1)
        """
        