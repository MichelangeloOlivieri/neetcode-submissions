class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # soluzione ottimale

        if len(s) != len(t):
            return False

        else:
            dictionary_s = {}
            dictionary_t = {}

            for i in range(len(s)):
                dictionary_s[s[i]] = dictionary_s.get(s[i], 0) + 1
                dictionary_t[t[i]] = dictionary_t.get(t[i], 0) + 1

            for c in dictionary_s:
                if dictionary_s[c] != dictionary_t.get(c, 0):
                    return False

            return True



        