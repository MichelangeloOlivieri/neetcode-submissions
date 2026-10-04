class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""
        if len(strs) == 1:
            return strs[0]

        res = []
        j = 0

        while j < len(strs[0]):
            c = strs[0][j]
            for i in range(1, len(strs)):
                string = strs[i]
                if j == len(string) or string[j] != c:
                    return "".join(res)
                if i == len(strs) - 1:
                    res.append(c)
            j += 1

        return "".join(res)

        """
        - Time complexity O(m), where m = #{characters}
        - Space complexity O(n), where n = #{unique characters across strings}
        """