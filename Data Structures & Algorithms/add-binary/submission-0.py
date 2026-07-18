class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # ==========================================
        # Clarifying Questions:
        # 1. Are native type conversions like int(x, 2) permitted? (Assuming no, hardware logic required).
        # 2. Are there leading zeros? (No).
        #
        # Algorithm Description:
        # Two-pointer simulation of a hardware Full Adder from right to left. 
        # Results are buffered in an array to ensure O(1) operations, avoiding O(N^2) string concatenation penalties.
        # ==========================================

        res = []
        i = len(a) - 1
        j = len(b) - 1
        carry = 0

        while i >= 0 or j >= 0 or carry:
            total_sum = carry

            if i >= 0:
                total_sum += int(a[i])
                i -= 1

            if j >= 0:
                total_sum += int(b[j])
                j -= 1

            res.append(str(total_sum % 2))
            carry = total_sum // 2

        res.reverse()
        return "".join(res)

        # ==========================================
        # Time Complexity: O(max(N, M)), where N and M are the lengths of strings a and b.
        # Space Complexity: O(max(N, M)) strictly for the output structure. Auxiliary space is O(1).
        # ==========================================