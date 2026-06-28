class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        """
        1) Only possible if h >= len(piles)
        2) Binary search solution
        """

        if not piles:
            return 0

        l = 1
        r = max(piles)

        if r < l:
            return r

        while l <= r:
            mid = (l + r) // 2
            hours = sum(((piles[i] - 1) // mid) + 1 for i in range(len(piles)))

            if hours <= h:
                r = mid - 1
            else:
                l = mid + 1

        return l

        """
        3) Ok
        4) Time complexity O(log(max(piles)) * len(piles))
        """
