class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        m = len(str1)
        n = len(str2)

        def isDivisor(l):
            if m % l or n % l or str1[: l] != str2[: l]:
                return False

            a = m // l
            b = n // l
            return str1[: l] * a == str1 and str2[: l] * b == str2

        for l in range(min(m, n), 0, -1):
            if isDivisor(l):
                return str1[: l]
            
        return ""

        """
        - Time complexity O(min(m, n) * (m + n)), where m = len(str1) and n = len(str2)
        - Space complexity O(m + n)
        """