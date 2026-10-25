class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m * n != len(original):
            return []

        res = []

        for i in range(m):
            res.append([])
            for j in range(n):
                res[i].append(original[i * n + j])

        return res
        
        """
        - Time complexity O(n), where n = len(original)
        - Space complexity O(n) (for the result matrix)
        """