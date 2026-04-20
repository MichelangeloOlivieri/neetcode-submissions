class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        first_dict = {}
        for c in s:
            first_dict[c] = first_dict.get(c, 0) + 1
        second_dict = {}
        for c in t:
            second_dict[c] = second_dict.get(c, 0) + 1

        for c in first_dict:
            if first_dict[c] != second_dict.get(c, 0):
                return False

        return True