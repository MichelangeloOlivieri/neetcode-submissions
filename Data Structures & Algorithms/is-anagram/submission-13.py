class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if not s and not t:
            return True
        if not s or not t or len(s) != len(t):
            return False

        first_dict = {}
        for c in s:
            first_dict[c] = first_dict.get(c, 0) + 1
        second_dict = {}
        for c in t:
            second_dict[c] = second_dict.get(c, 0) + 1

        return first_dict == second_dict