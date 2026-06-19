class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)

        if not piles or r == 0:
            return 0

        while l <= r:
            mid = (l + r) // 2
            if mid != 0:
                hours = sum((p - 1) // mid + 1 for p in piles)
            else:
                hours = float('inf')

            if hours > h:
                l = mid + 1
            else:
                r = mid - 1

        return l

        """
        Time complexity O(n * log(h)); space complexity O(1)
        """
        