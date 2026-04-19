class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # edge cases

        if len(t) > len(s) or t == "":
            return ""

        # implementation

        count_t = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        l = 0
        r = 0
        have = 0
        need = len(count_t)
        window = {}
        res_length = float('inf')
        res_id = [-1, -1]

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in count_t and window[s[r]] == count_t[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < res_length:
                    res_length = r - l + 1
                    res_id = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] == count_t[s[l]] - 1:
                    have -= 1
                l += 1

        left = res_id[0]
        right = res_id[1]

        return s[left: right + 1] if res_length != float('inf') else ""

        




        