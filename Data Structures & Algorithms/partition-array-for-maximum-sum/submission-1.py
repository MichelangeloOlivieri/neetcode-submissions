class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:

        if not arr:
            return 0

        n = len(arr)
        best = [0] * (n + 1)

        for end in range(1, n + 1):
            largest = 0
            for length in range(1, min(k, end) + 1):
                largest = max(largest, arr[end - length])
                best[end] = max(best[end], best[end - length] + largest * length)

        return best[n]

        """
        - Time complexity O(n * k), where n = len(arr)
        - Space complexity O(n)
        """