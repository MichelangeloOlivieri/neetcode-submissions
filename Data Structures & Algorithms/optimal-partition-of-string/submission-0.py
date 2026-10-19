class Solution:
    def partitionString(self, s: str) -> int:

        if not s:
            return 0

        count = 1
        seen = set()

        for c in s:
            if c in seen:
                for d in seen.copy():
                    seen.remove(d)
                count += 1
            seen.add(c)

        return count

        """
        - Time complexity O(n), where n = len(s)
        - Space complexity O(n)
        """